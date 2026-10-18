# ViThunkCreateThunkTable

- RVA: `0x00BA74DC`–`0x00BA7555` (길이 `121` bytes)
- VA: `0x0000000140BA74DC`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E6B4`
- 디코드: `35`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA7513` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00BA752A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [VfThunkAddDriverThunks](VfThunkAddDriverThunks_function_00BA6E2C.md) at `0x00BA6E45`
- [VfThunkAddSpecialDriverThunks](VfThunkAddSpecialDriverThunks_function_00BA6EC4.md) at `0x00BA6EEC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00BA7513` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGEVRFY` → `POOLCODE`)
  - `0x00BA752A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA74DC  48 8B C4                        mov rax, rsp
00BA74DF  48 89 58 08                     mov qword ptr [rax + 8], rbx
00BA74E3  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00BA74E7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00BA74EB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00BA74EF  41 56                           push r14
00BA74F1  48 83 EC 20                     sub rsp, 0x20
00BA74F5  8B FA                           mov edi, edx
00BA74F7  49 8B E8                        mov rbp, r8
00BA74FA  4C 8B F1                        mov r14, rcx
00BA74FD  C1 EF 04                        shr edi, 4
00BA7500  8B F7                           mov esi, edi
00BA7502  B9 00 01 00 00                  mov ecx, 0x100
00BA7507  C1 E6 04                        shl esi, 4
00BA750A  41 B8 4D 6D 56 74               mov r8d, 0x74566d4d
00BA7510  8D 56 20                        lea edx, [rsi + 0x20]
00BA7513  E8 D8 AB FD FF                  call 0x140b820f0
00BA7518  48 8B D8                        mov rbx, rax
00BA751B  48 85 C0                        test rax, rax
00BA751E  74 19                           je 0x140ba7539
00BA7520  44 8B C6                        mov r8d, esi
00BA7523  48 8D 48 20                     lea rcx, [rax + 0x20]
00BA7527  49 8B D6                        mov rdx, r14
00BA752A  E8 11 F3 B1 FF                  call 0x1406c6840
00BA752F  48 8B C3                        mov rax, rbx
00BA7532  48 89 6B 10                     mov qword ptr [rbx + 0x10], rbp
00BA7536  89 7B 18                        mov dword ptr [rbx + 0x18], edi
00BA7539  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BA753E  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00BA7543  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BA7548  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00BA754D  48 83 C4 20                     add rsp, 0x20
00BA7551  41 5E                           pop r14
00BA7553  C3                              ret
00BA7554  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViThunkCreateThunkTable(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
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
    v_rdi = (unsigned int)(((unsigned int)(a2)) >> (4));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) << (4));
    result = ExAllocatePool2(256, v_rsi + 32, (unsigned int)(0x74566D4DULL), a4);
    if (result != 0) {
        a3 = (unsigned int)(v_rsi);
        a1 = result + 32;
        a2 = a1;
        result = memcpy(a1, a2, a3, a4);
        result = result;
        *(unsigned __int64 *)(result + 16) = a3;
        *(unsigned int *)(result + 24) = (unsigned int)(v_rdi);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViThunkCreateThunkTable(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
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
    local_rdi = (uint32_t)(((uint32_t)(Arg2)) >> (4));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) << (4));
    result = ExAllocatePool2(256, local_rsi + 32, (uint32_t)(0x74566D4DULL), a4);
    if (result != 0) {
        Arg3 = (uint32_t)(local_rsi);
        Arg1 = result + 32;
        Arg2 = Arg1;
        result = memcpy(Arg1, Arg2, Arg3, a4);
        result = result;
        *(uint64_t *)(result + 0x10) = Arg3;
        *(uint32_t *)(result + 0x18) = (uint32_t)(local_rdi);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA74DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA74DC[BB_00BA74DC]
  bb_00BA7520[BB_00BA7520]
  bb_00BA7539[BB_00BA7539]
  bb_00BA7554[BB_00BA7554]
  bb_00BA74DC -->|branch| bb_00BA7539
  bb_00BA74DC -->|fallthrough| bb_00BA7520
  bb_00BA7520 -->|flow| bb_00BA7539
```
