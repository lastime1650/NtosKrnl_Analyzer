# ObInitializeFastReference

- RVA: `0x009F0D24`–`0x009F0D63` (길이 `63` bytes)
- VA: `0x00000001409F0D24`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `20`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009F0D42` → [ObpIncrPointerCountEx](../../text/41/ObpIncrPointerCountEx_function_00419CB0.md) (function, `0x00419CB0`)

### Direct callers
- [PspLocateSystemDll](../77/PspLocateSystemDll_function_0077F0D0.md) at `0x0077F27E`
- [PspAllocateThread](../9E/PspAllocateThread_function_009EF72C.md) at `0x009EFE46`
- [SeAssignPrimaryToken](SeAssignPrimaryToken_function_009F117C.md) at `0x009F1231`
- [PspInitializeProcessSecurity](../AA/PspInitializeProcessSecurity_function_00AAD368.md) at `0x00AAD478`
- [SepInitializationPhase0](../../init/C4/SepInitializationPhase0_function_00C4A790.md) at `0x00C4A7F1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009F0D42` → [ObpIncrPointerCountEx](../../text/41/ObpIncrPointerCountEx_function_00419CB0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F0D24  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009F0D29  57                              push rdi
009F0D2A  48 83 EC 20                     sub rsp, 0x20
009F0D2E  48 8B DA                        mov rbx, rdx
009F0D31  48 8B F9                        mov rdi, rcx
009F0D34  48 85 D2                        test rdx, rdx
009F0D37  74 0E                           je 0x1409f0d47
009F0D39  48 8D 4A D0                     lea rcx, [rdx - 0x30]
009F0D3D  BA 0F 00 00 00                  mov edx, 0xf
009F0D42  E8 69 8F A2 FF                  call 0x140419cb0
009F0D47  4C 8D 43 0F                     lea r8, [rbx + 0xf]
009F0D4B  48 F7 DB                        neg rbx
009F0D4E  48 1B C0                        sbb rax, rax
009F0D51  49 23 C0                        and rax, r8
009F0D54  48 89 07                        mov qword ptr [rdi], rax
009F0D57  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009F0D5C  48 83 C4 20                     add rsp, 0x20
009F0D60  5F                              pop rdi
009F0D61  C3                              ret
009F0D62  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObInitializeFastReference(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (a2 != 0) {
        a1 = a2 - 48;
        a2 = 15;
        result = ObpIncrPointerCountEx(a1, a2, a3, a4);
    }
    v_rbx = -(a2);
    result = (result) & (a2 + 15);
    *(unsigned __int64 *)(a1) = result;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObInitializeFastReference(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (Arg2 != NULL) {
        Arg1 = Arg2 - 48;
        Arg2 = 15;
        result = ObpIncrPointerCountEx(Arg1, Arg2, a3, a4);
    }
    local_rbx = -(Arg2);
    result = (result) & (Arg2 + 15);
    *(uint64_t *)(arg1) = result;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0xF` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F0D24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009F0D24[BB_009F0D24]
  bb_009F0D39[BB_009F0D39]
  bb_009F0D47[BB_009F0D47]
  bb_009F0D62[BB_009F0D62]
  bb_009F0D24 -->|branch| bb_009F0D47
  bb_009F0D24 -->|fallthrough| bb_009F0D39
  bb_009F0D39 -->|flow| bb_009F0D47
```
