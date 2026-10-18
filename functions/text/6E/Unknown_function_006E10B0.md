# sub_006E10B0

- RVA: `0x006E10B0`–`0x006E112E` (길이 `126` bytes)
- VA: `0x00000001406E10B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074538`
- 디코드: `31`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006E1105` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x006E110D` → [MmGetPhysicalAddress](../23/MmGetPhysicalAddress_function_0023A500.md) (function, `0x0023A500`)
- `0x006E1123` → [VslFlushSecureAddressSpace](../4B/VslFlushSecureAddressSpace_function_004BC6FC.md) (function, `0x004BC6FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006E10F9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006E111E` → [sub_00312CF6 + 0x6A](../31/Unknown_function_00312CF6.md) (`tail-transfer`)
  - `0x006E1129` → [sub_00312CF6 + 0x12F](../31/Unknown_function_00312CF6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E10B0  48 8D 4D 07                     lea rcx, [rbp + 7]
006E10B4  41 B9 02 00 00 00               mov r9d, 2
006E10BA  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
006E10BE  4C 8D 79 17                     lea r15, [rcx + 0x17]
006E10C2  49 8B C7                        mov rax, r15
006E10C5  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
006E10CC  48 33 C1                        xor rax, rcx
006E10CF  48 A9 00 F0 FF FF               test rax, -0x1000
006E10D5  41 8B C1                        mov eax, r9d
006E10D8  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
006E10DC  4C 0F 44 F9                     cmove r15, rcx
006E10E0  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
006E10E4  44 0F 20 C0                     mov rax, cr8
006E10E8  88 44 24 60                     mov byte ptr [rsp + 0x60], al
006E10EC  41 3A C1                        cmp al, r9b
006E10EF  73 19                           jae 0x1406e110a
006E10F1  44 0F 20 C1                     mov rcx, cr8
006E10F5  45 0F 22 C1                     mov cr8, r9
006E10F9  39 1D 21 5C 8E 00               cmp dword ptr [rip + 0x8e5c21], ebx
006E10FF  74 09                           je 0x1406e110a
006E1101  41 0F B6 D1                     movzx edx, r9b
006E1105  E8 F2 45 E1 FF                  call 0x1404f56fc
006E110A  49 8B CF                        mov rcx, r15
006E110D  E8 EE 93 B5 FF                  call 0x14023a500
006E1112  48 8B F8                        mov rdi, rax
006E1115  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
006E111A  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
006E111E  E9 3D 1C C3 FF                  jmp 0x140312d60
006E1123  E8 D4 B5 DD FF                  call 0x1404bc6fc
006E1128  90                              nop
006E1129  E9 F7 1C C3 FF                  jmp 0x140312e25
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E10B0(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_r15;
    unsigned int v_stack_p48;
    unsigned int v_stack_p58;
    unsigned __int8 v_stack_p60;
    unsigned __int64 v_stack_p70;

    a1 = (v_rbp + 7) & (-8);
    v_r15 = (a1 + 23) & (0xFFFFFFFFFFFFF000ULL);
    result = (a1 + 23) ^ (a1);
    v_stack_p48 = 2;
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) == 0) { v_r15 = a1; }
    v_stack_p58 = 2;
    v_stack_p60 = (unsigned __int8)(v_cr8);
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_006E110A;
    result = v_cr8;
    if ((*(unsigned int *)(v_rip + 9329697)) != ((unsigned int)(v_rbx))) {
        a2 = 2;
        result = KiRaiseIrqlProcessIrqlFlags(v_cr8, a2, a3, 2);
    }
    result = MmGetPhysicalAddress(v_r15, a2, a3, 2);
    v_stack_p70 = result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E10B0(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint32_t Arg9)
{
    int64_t result;
    int64_t local_r15;
    uint32_t v_stack_p48;
    uint32_t v_stack_p58;
    uint8_t v_stack_p60;
    uint64_t v_stack_p70;

    Arg1 = (local_rbp + 7) & (-8);
    local_r15 = (Arg1 + 23) & (0xFFFFFFFFFFFFF000ULL);
    result = (Arg1 + 23) ^ (Arg1);
    v_stack_p48 = 2;
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) == 0) { local_r15 = Arg1; }
    v_stack_p58 = 2;
    v_stack_p60 = (uint8_t)(v_cr8);
    if (((uint8_t)(v_cr8)) >= 2) goto loc_006E110A;
    result = v_cr8;
    if ((*(uint32_t *)(v_rip + 0x8E5C21)) != ((uint32_t)(local_rbx))) {
        Arg2 = 2;
        result = KiRaiseIrqlProcessIrqlFlags(v_cr8, Arg2, Arg3, 2);
    }
    result = MmGetPhysicalAddress(local_r15, Arg2, Arg3, 2);
    v_stack_p70 = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E10B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E10B0[BB_006E10B0]
  bb_006E10F1[BB_006E10F1]
  bb_006E1101[BB_006E1101]
  bb_006E110A[BB_006E110A]
  bb_006E1123[BB_006E1123]
  bb_006E10B0 -->|branch| bb_006E110A
  bb_006E10B0 -->|fallthrough| bb_006E10F1
  bb_006E10F1 -->|branch| bb_006E110A
  bb_006E10F1 -->|fallthrough| bb_006E1101
  bb_006E1101 -->|flow| bb_006E110A
```
