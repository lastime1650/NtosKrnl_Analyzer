# MiReturnEnclavePage

- RVA: `0x004DEEF8`–`0x004DEF66` (길이 `110` bytes)
- VA: `0x00000001404DEEF8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `28`개 명령, `110/110` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004DEF22` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x004DEF46` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x004DEF50` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiAddPagesToEnclave](../36/MiAddPagesToEnclave_function_00367EEC.md) at `0x00368264`
- [MiPrepareEnclaveMetadataPage](../68/MiPrepareEnclaveMetadataPage_function_00686EAC.md) at `0x0068706D`
- [sub_006E7C8A](../6E/Unknown_function_006E7C8A.md) at `0x006E7CA2`
- [MiCopyPagesIntoEnclave](../../page/A4/MiCopyPagesIntoEnclave_function_00A472AC.md) at `0x00A478C3`
- [MiReleaseEnclaveMetadataPage](../../pagelk/B7/MiReleaseEnclaveMetadataPage_function_00B74EE4.md) at `0x00B74F33`
- [MiReturnReservedEnclavePages](../../pagelk/B7/MiReturnReservedEnclavePages_function_00B74FD0.md) at `0x00B75012`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004DEEF8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004DEEFD  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
004DEF02  57                              push rdi
004DEF03  48 83 EC 20                     sub rsp, 0x20
004DEF07  48 8D 34 49                     lea rsi, [rcx + rcx*2]
004DEF0B  48 8B F9                        mov rdi, rcx
004DEF0E  48 C1 E6 04                     shl rsi, 4
004DEF12  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004DEF1C  48 03 F0                        add rsi, rax
004DEF1F  48 8B CE                        mov rcx, rsi
004DEF22  E8 19 B4 E3 FF                  call 0x14031a340
004DEF27  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
004DEF2B  8A D8                           mov bl, al
004DEF2D  48 B8 00 00 00 00 00 FF FF FF   movabs rax, 0xffffff0000000000
004DEF37  48 8B CF                        mov rcx, rdi
004DEF3A  48 23 D0                        and rdx, rax
004DEF3D  48 89 56 18                     mov qword ptr [rsi + 0x18], rdx
004DEF41  BA 00 01 00 00                  mov edx, 0x100
004DEF46  E8 D5 5D E5 FF                  call 0x140334d20
004DEF4B  8A D3                           mov dl, bl
004DEF4D  48 8B CE                        mov rcx, rsi
004DEF50  E8 8B B4 E3 FF                  call 0x14031a3e0
004DEF55  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004DEF5A  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
004DEF5F  48 83 C4 20                     add rsp, 0x20
004DEF63  5F                              pop rdi
004DEF64  C3                              ret
004DEF65  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReturnEnclavePage(__int64 a1)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rsi = (a1 + a1 * 2) << (4);
    v_rsi = (v_rsi) + (result);
    result = MiLockPageInline(v_rsi, a2, a3, a4);
    a2 = (*(unsigned __int64 *)(v_rsi + 24)) & (result);
    *(unsigned __int64 *)(v_rsi + 24) = a2;
    result = MiInsertPageInFreeOrZeroedList(a1, 256, a3, a4);
    result = MiUnlockPage(v_rsi, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReturnEnclavePage(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rsi = (Arg1 + Arg1 * 2) << (4);
    local_rsi = (local_rsi) + (result);
    result = MiLockPageInline(local_rsi, a2, a3, a4);
    a2 = (*(uint64_t *)(local_rsi + 0x18)) & (result);
    *(uint64_t *)(local_rsi + 0x18) = a2;
    result = MiInsertPageInFreeOrZeroedList(Arg1, 256, a3, a4);
    result = MiUnlockPage(local_rsi, (uint8_t)((uint8_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004DEEF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004DEEF8[BB_004DEEF8]
  bb_004DEF65[BB_004DEF65]
```
