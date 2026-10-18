# MmStoreFreeVirtualMemory

- RVA: `0x00A767A8`–`0x00A7684C` (길이 `164` bytes)
- VA: `0x0000000140A767A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AE1B4`
- 디코드: `43`개 명령, `164/164` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A767C5` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x00A767FA` → [MiUnlockPageTableRange](../../text/40/MiUnlockPageTableRange_function_00407E44.md) (function, `0x00407E44`)
- `0x00A76831` → [MiFreeVadRange](../../text/2A/MiFreeVadRange_function_002A77AC.md) (function, `0x002A77AC`)

### Direct callers
- [SmKmStoreHelperCommandProcess](../../text/3C/SmKmStoreHelperCommandProcess_function_003C3AA4.md) at `0x003C3C46`
- [sub_006E8004](../../text/6E/Unknown_function_006E8004.md) at `0x006E80D4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A767C5` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (`PAGE` → `.text`)
  - `0x00A767FA` → [MiUnlockPageTableRange](../../text/40/MiUnlockPageTableRange_function_00407E44.md) (`PAGE` → `.text`)
  - `0x00A76831` → [MiFreeVadRange](../../text/2A/MiFreeVadRange_function_002A77AC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A767A8  48 8B C4                        mov rax, rsp
00A767AB  48 89 58 08                     mov qword ptr [rax + 8], rbx
00A767AF  48 89 68 18                     mov qword ptr [rax + 0x18], rbp
00A767B3  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
00A767B7  57                              push rdi
00A767B8  48 83 EC 40                     sub rsp, 0x40
00A767BC  4C 8D 40 10                     lea r8, [rax + 0x10]
00A767C0  33 D2                           xor edx, edx
00A767C2  48 8B F9                        mov rdi, rcx
00A767C5  E8 C6 FE 89 FF                  call 0x140316690
00A767CA  48 8B E8                        mov rbp, rax
00A767CD  8B 48 1C                        mov ecx, dword ptr [rax + 0x1c]
00A767D0  8B 50 18                        mov edx, dword ptr [rax + 0x18]
00A767D3  0F B6 58 21                     movzx ebx, byte ptr [rax + 0x21]
00A767D7  0F B6 70 20                     movzx esi, byte ptr [rax + 0x20]
00A767DB  48 C1 E3 20                     shl rbx, 0x20
00A767DF  48 0B D9                        or rbx, rcx
00A767E2  48 C1 E6 20                     shl rsi, 0x20
00A767E6  48 0B F2                        or rsi, rdx
00A767E9  48 8B CF                        mov rcx, rdi
00A767EC  48 8B D3                        mov rdx, rbx
00A767EF  48 C1 E2 0C                     shl rdx, 0xc
00A767F3  48 81 CA FF 0F 00 00            or rdx, 0xfff
00A767FA  E8 45 16 99 FF                  call 0x140407e44
00A767FF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A76808  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00A7680D  33 C9                           xor ecx, ecx
00A7680F  4C 8B CB                        mov r9, rbx
00A76812  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A76817  4C 8B C6                        mov r8, rsi
00A7681A  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00A7681E  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00A76825  88 4C 24 58                     mov byte ptr [rsp + 0x58], cl
00A76829  48 8B CD                        mov rcx, rbp
00A7682C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A76831  E8 76 0F 83 FF                  call 0x1402a77ac
00A76836  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00A7683B  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
00A76840  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00A76845  48 83 C4 40                     add rsp, 0x40
00A76849  5F                              pop rdi
00A7684A  C3                              ret
00A7684B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmStoreFreeVirtualMemory(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (64);
    a2 = 0;
    result = MiObtainReferencedVadEx(a1, a2, v_rsp + 16, a4);
    v_rbx = (*(unsigned __int8 *)(result + 33)) << (32);
    v_rbx = (v_rbx) | ((unsigned int)(*(unsigned int *)(result + 28)));
    v_rsi = (*(unsigned __int8 *)(result + 32)) << (32);
    v_rsi = (v_rsi) | ((unsigned int)(*(unsigned int *)(result + 24)));
    a2 = (v_rbx) << (12);
    a2 = (a2) | (0xFFFULL);
    result = MiUnlockPageTableRange(a1, a2, v_rsp + 16, a4);
    a1 = 0;
    v_stack_m18 = 0;
    v_stack_m20 = 0;
    v_stack_p10 = 0;
    v_stack_m28 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = MiFreeVadRange(result, v_stack_p10, v_rsi, v_rbx);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmStoreFreeVirtualMemory(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (64);
    Arg2 = 0;
    result = MiObtainReferencedVadEx(Arg1, Arg2, local_rsp + 16, a4);
    local_rbx = (*(uint8_t *)(result + 0x21)) << (32);
    local_rbx = (local_rbx) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    local_rsi = (*(uint8_t *)(result + 0x20)) << (32);
    local_rsi = (local_rsi) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    Arg2 = (local_rbx) << (12);
    Arg2 = (Arg2) | (0xFFFULL);
    result = MiUnlockPageTableRange(Arg1, Arg2, local_rsp + 16, a4);
    Arg1 = 0;
    v_stack_m18 = 0;
    v_stack_m20 = 0;
    v_stack_p10 = 0;
    v_stack_m28 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = MiFreeVadRange(result, v_stack_p10, local_rsi, local_rbx);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A767A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A767A8[BB_00A767A8]
  bb_00A7684B[BB_00A7684B]
```
