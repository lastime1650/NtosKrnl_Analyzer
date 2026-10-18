# MiStoreModifiedWriteComplete

- RVA: `0x002045E8`–`0x0020468D` (길이 `165` bytes)
- VA: `0x00000001402045E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CB8C`
- 디코드: `43`개 명령, `165/165` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00204618` → [MiStoreFreeWriteSupport](MiStoreFreeWriteSupport_function_00203A48.md) (function, `0x00203A48`)
- `0x00204620` → [MiStoreModifiedWriteDereference](MiStoreModifiedWriteDereference_function_00203E94.md) (function, `0x00203E94`)
- `0x00204641` → [MiStoreLogWriteCompleteFailure](../4A/MiStoreLogWriteCompleteFailure_function_004A4414.md) (function, `0x004A4414`)
- `0x00204662` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00204671` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x0020467B` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmIoCtxWorkItemComplete](SMKM_STORE_MGR_SM_TRAITS_SmIoCtxWorkItemComplete_function_00205850.md) at `0x0020595B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002045E8  48 8B C4                        mov rax, rsp
002045EB  48 89 58 08                     mov qword ptr [rax + 8], rbx
002045EF  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
002045F3  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
002045F7  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
002045FB  41 56                           push r14
002045FD  48 83 EC 20                     sub rsp, 0x20
00204601  48 8B 29                        mov rbp, qword ptr [rcx]
00204604  48 8B F1                        mov rsi, rcx
00204607  8B 49 08                        mov ecx, dword ptr [rcx + 8]
0020460A  4C 8B 75 38                     mov r14, qword ptr [rbp + 0x38]
0020460E  85 C9                           test ecx, ecx
00204610  78 2F                           js 0x140204641
00204612  49 8B D6                        mov rdx, r14
00204615  48 8B CE                        mov rcx, rsi
00204618  E8 2B F4 FF FF                  call 0x140203a48
0020461D  48 8B CD                        mov rcx, rbp
00204620  E8 6F F8 FF FF                  call 0x140203e94
00204625  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0020462A  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0020462F  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00204634  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00204639  48 83 C4 20                     add rsp, 0x20
0020463D  41 5E                           pop r14
0020463F  C3                              ret
00204640  CC                              int3
00204641  E8 CE FD 29 00                  call 0x1404a4414
00204646  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
0020464A  48 8D 3C 40                     lea rdi, [rax + rax*2]
0020464E  48 C1 E7 04                     shl rdi, 4
00204652  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0020465C  48 03 F8                        add rdi, rax
0020465F  48 8B CF                        mov rcx, rdi
00204662  E8 D9 5C 11 00                  call 0x14031a340
00204667  BA 01 00 00 00                  mov edx, 1
0020466C  48 8B CF                        mov rcx, rdi
0020466F  8A D8                           mov bl, al
00204671  E8 EA E2 15 00                  call 0x140362960
00204676  8A D3                           mov dl, bl
00204678  48 8B CF                        mov rcx, rdi
0020467B  E8 60 5D 11 00                  call 0x14031a3e0
00204680  41 C7 86 C4 04 00 00 20 00 00 00  mov dword ptr [r14 + 0x4c4], 0x20
0020468B  EB 85                           jmp 0x140204612
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiStoreModifiedWriteComplete(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (32);
    if (sign_flag) goto loc_00204641;
loc_00204612:
    result = MiStoreFreeWriteSupport(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56), a3, a4);
    result = MiStoreModifiedWriteDereference(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00204641:
    result = MiStoreLogWriteCompleteFailure(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56), a3, a4);
    v_rdi = (*(unsigned __int64 *)(v_stack_p18 + 80) + *(unsigned __int64 *)(v_stack_p18 + 80) * 2) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_stack_p18 + 80));
    result = MiLockPageInline(v_rdi, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56), a3, a4);
    result = MiSetPfnModified(v_rdi, 1, a3, a4);
    result = MiUnlockPage(v_rdi, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) + 1220) = 32;
    goto loc_00204612;
}
```

## 5. (Beta) C Style

```c
int64_t MiStoreModifiedWriteComplete(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (32);
    if (sign_flag) goto loc_00204641;
loc_00204612:
    result = MiStoreFreeWriteSupport(Arg1, *(uint64_t *)(*(uint64_t *)(arg1) + 0x38), a3, a4);
    result = MiStoreModifiedWriteDereference(*(uint64_t *)(arg1), *(uint64_t *)(*(uint64_t *)(arg1) + 0x38), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00204641:
    result = MiStoreLogWriteCompleteFailure(*(uint64_t *)(arg1), *(uint64_t *)(*(uint64_t *)(arg1) + 0x38), a3, a4);
    local_rdi = (*(uint64_t *)(v_stack_p18 + 0x50) + *(uint64_t *)(v_stack_p18 + 0x50) * 2) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_stack_p18 + 0x50));
    result = MiLockPageInline(local_rdi, *(uint64_t *)(*(uint64_t *)(arg1) + 0x38), a3, a4);
    result = MiSetPfnModified(local_rdi, 1, a3, a4);
    result = MiUnlockPage(local_rdi, (uint8_t)((uint8_t)(result)), a3, a4);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x38) + 0x4C4) = 32;
    goto loc_00204612;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002045E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002045E8[BB_002045E8]
  bb_00204612[BB_00204612]
  bb_00204640[BB_00204640]
  bb_00204641[BB_00204641]
  bb_002045E8 -->|branch| bb_00204641
  bb_002045E8 -->|fallthrough| bb_00204612
  bb_00204640 -->|flow| bb_00204641
  bb_00204641 -->|branch| bb_00204612
```
