# MiCountCommittedPages

- RVA: `0x002C7950`–`0x002C79CE` (길이 `126` bytes)
- VA: `0x00000001402C7950`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `36`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002C7978` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C799C` → [MiComputePageCommitment](MiComputePageCommitment_function_002C5C34.md) (function, `0x002C5C34`)
- `0x002C79AA` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)

### Direct callers
- [MiCopyPagesIntoEnclave](../../page/A4/MiCopyPagesIntoEnclave_function_00A472AC.md) at `0x00A4741A`
- [MiLoadSectionIntoVsmEnclave](../../page/AB/MiLoadSectionIntoVsmEnclave_function_00AB1D4C.md) at `0x00AB1E9A`
- [MiLoadDataIntoVsmEnclave](../../page/AC/MiLoadDataIntoVsmEnclave_function_00ACD114.md) at `0x00ACD2B9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C7950  48 8B C4                        mov rax, rsp
002C7953  48 89 58 08                     mov qword ptr [rax + 8], rbx
002C7957  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
002C795B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
002C795F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
002C7963  41 56                           push r14
002C7965  48 83 EC 40                     sub rsp, 0x40
002C7969  48 8B E9                        mov rbp, rcx
002C796C  4D 8B F1                        mov r14, r9
002C796F  49 8B C9                        mov rcx, r9
002C7972  49 8B D8                        mov rbx, r8
002C7975  48 8B F2                        mov rsi, rdx
002C7978  E8 73 52 FB FF                  call 0x14027cbf0
002C797D  40 8A F8                        mov dil, al
002C7980  4C 8B C3                        mov r8, rbx
002C7983  33 C0                           xor eax, eax
002C7985  44 8A CF                        mov r9b, dil
002C7988  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002C798D  48 8B D6                        mov rdx, rsi
002C7990  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002C7995  48 8B CD                        mov rcx, rbp
002C7998  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002C799C  E8 93 E2 FF FF                  call 0x1402c5c34
002C79A1  40 8A D7                        mov dl, dil
002C79A4  49 8B CE                        mov rcx, r14
002C79A7  48 8B D8                        mov rbx, rax
002C79AA  E8 E1 5C FB FF                  call 0x14027d690
002C79AF  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
002C79B4  48 8B C3                        mov rax, rbx
002C79B7  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
002C79BC  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002C79C1  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
002C79C6  48 83 C4 40                     add rsp, 0x40
002C79CA  41 5E                           pop r14
002C79CC  C3                              ret
002C79CD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCountCommittedPages(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = MiLockWorkingSetShared(a4, a2, a3, a4);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m20 = 0;
    v_stack_m28 = 0;
    result = MiComputePageCommitment(a1, a2, a3, (unsigned __int8)((unsigned __int8)(result)));
    result = MiUnlockWorkingSetShared(a4, (unsigned __int8)((unsigned __int8)(result)), a3, (unsigned __int8)((unsigned __int8)(result)));
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiCountCommittedPages(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = MiLockWorkingSetShared(Arg4, Arg2, Arg3, Arg4);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m20 = 0;
    v_stack_m28 = 0;
    result = MiComputePageCommitment(Arg1, Arg2, Arg3, (uint8_t)((uint8_t)(result)));
    result = MiUnlockWorkingSetShared(Arg4, (uint8_t)((uint8_t)(result)), Arg3, (uint8_t)((uint8_t)(result)));
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C7950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C7950[BB_002C7950]
  bb_002C79CD[BB_002C79CD]
```
