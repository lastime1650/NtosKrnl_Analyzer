# MiDecommitPages

- RVA: `0x00241BD0`–`0x00241C55` (길이 `133` bytes)
- VA: `0x0000000140241BD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061934`
- 디코드: `32`개 명령, `133/133` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00241BFC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00241C42` → [MiDecommitInitializePacket](MiDecommitInitializePacket_function_00242F30.md) (function, `0x00242F30`)

### Direct callers
- [MiMapImageScpCfgPages](../29/MiMapImageScpCfgPages_function_00294FA4.md) at `0x002950CC`
- [MiRemoveMappedPtes](../29/MiRemoveMappedPtes_function_00296A50.md) at `0x00296B42`
- [MmFreePoolMemory](../2C/MmFreePoolMemory_function_002C1578.md) at `0x002C166E`
- [MiDeleteKernelStackPages](../2D/MiDeleteKernelStackPages_function_002D9938.md) at `0x002D99AE`
- [MmStoreDecommitVirtualMemory](../47/MmStoreDecommitVirtualMemory_function_00474BF0.md) at `0x00474C8F`
- [MiDeleteBootRange](../66/MiDeleteBootRange_function_0066E450.md) at `0x0066E4EA`
- [MiFreeInitializationCode](../../page/7F/MiFreeInitializationCode_function_007F88A0.md) at `0x007F8AE3`
- [MiDecommitRegion](../../page/88/MiDecommitRegion_function_008807A0.md) at `0x00880835`
- [MmStoreAllocateVirtualMemory](../../page/A6/MmStoreAllocateVirtualMemory_function_00A68238.md) at `0x00A68397`
- [MiUnloadSystemImage](../../page/AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA32B7`
- [MmReturnChargesToLockPagedPool](../../page/AD/MmReturnChargesToLockPagedPool_function_00AD3A00.md) at `0x00AD3A68`
- [MiFreeBootDriverPages](../../init/C7/MiFreeBootDriverPages_function_00C7695C.md) at `0x00C76BFF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00241C4F` → [sub_00241E74](Unknown_function_00241E74.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00241BD0  40 55                           push rbp
00241BD2  53                              push rbx
00241BD3  56                              push rsi
00241BD4  57                              push rdi
00241BD5  41 56                           push r14
00241BD7  48 8D 6C 24 B0                  lea rbp, [rsp - 0x50]
00241BDC  48 81 EC 50 01 00 00            sub rsp, 0x150
00241BE3  49 8B F8                        mov rdi, r8
00241BE6  48 8B F2                        mov rsi, rdx
00241BE9  4C 8B F1                        mov r14, rcx
00241BEC  33 D2                           xor edx, edx
00241BEE  41 B8 E0 00 00 00               mov r8d, 0xe0
00241BF4  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00241BF9  49 8B D9                        mov rbx, r9
00241BFC  E8 3F 50 48 00                  call 0x1406c6c40
00241C01  48 8B 85 B8 00 00 00            mov rax, qword ptr [rbp + 0xb8]
00241C08  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00241C0D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00241C12  4C 8B CF                        mov r9, rdi
00241C15  48 8B 85 B0 00 00 00            mov rax, qword ptr [rbp + 0xb0]
00241C1C  4C 8B C6                        mov r8, rsi
00241C1F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00241C24  49 8B D6                        mov rdx, r14
00241C27  8B 85 A8 00 00 00               mov eax, dword ptr [rbp + 0xa8]
00241C2D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00241C31  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
00241C38  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00241C3D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00241C42  E8 E9 12 00 00                  call 0x140242f30
00241C47  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00241C4B  48 39 45 A8                     cmp qword ptr [rbp - 0x58], rax
00241C4F  0F 87 1F 02 00 00               ja 0x140241e74
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDecommitPages(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;

    v_rsp = (v_rsp) - (336);
    a2 = 0;
    result = memset(v_stack_m118, a2, 224, a4);
    v_stack_m138 = a8;
    v_stack_m140 = a7;
    v_stack_m148 = (unsigned int)((unsigned int)(a6));
    v_stack_m150 = a5;
    v_stack_m158 = a4;
    result = MiDecommitInitializePacket(v_stack_m118, a1, 0, a3);
}
```

## 5. (Beta) C Style

```c
int64_t MiDecommitPages(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m78;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;

    local_rsp = (local_rsp) - (336);
    Arg2 = 0;
    result = memset(v_stack_m118, Arg2, 224, Arg4);
    v_stack_m138 = Arg8;
    v_stack_m140 = Arg7;
    v_stack_m148 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m150 = Arg5;
    v_stack_m158 = Arg4;
    result = MiDecommitInitializePacket(v_stack_m118, Arg1, 0, Arg3);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00241BD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00241BD0[BB_00241BD0]
```
