# PopEnlargeHiberFile

- RVA: `0x0075D564`–`0x0075D5F6` (길이 `146` bytes)
- VA: `0x000000014075D564`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `38`개 명령, `146/146` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0075D58D` → [MmGetNumberOfPhysicalPages](../../text/46/MmGetNumberOfPhysicalPages_function_00467F80.md) (function, `0x00467F80`)
- `0x0075D5A6` → [PopResizeHiberFile](../A9/PopResizeHiberFile_function_00A90410.md) (function, `0x00A90410`)

### Direct callers
- [sub_00B8053E](../../pagelk/B8/Unknown_function_00B8053E.md) at `0x00B80542`

### Static image references
- `0x0075D56E` → RVA `0x00F0BF30` (`.data`; read)
- `0x0075D586` → RVA `0x00F0DDC8` (`.data`; write)
- `0x0075D5BC` → RVA `0x00F0DDD8` (`.data`; write)
- `0x0075D5C3` → RVA `0x00F0DDE0` (`.data`; write)
- `0x0075D5CA` → RVA `0x00F0DDD0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0075D58D` → [MmGetNumberOfPhysicalPages](../../text/46/MmGetNumberOfPhysicalPages_function_00467F80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0075D564  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0075D569  57                              push rdi
0075D56A  48 83 EC 20                     sub rsp, 0x20
0075D56E  48 8B 05 BB E9 7A 00            mov rax, qword ptr [rip + 0x7ae9bb]
0075D575  48 8B F9                        mov rdi, rcx
0075D578  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
0075D57E  33 C9                           xor ecx, ecx
0075D580  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
0075D586  48 89 05 3B 08 7B 00            mov qword ptr [rip + 0x7b083b], rax
0075D58D  E8 EE A9 D0 FF                  call 0x140467f80
0075D592  48 8B D8                        mov rbx, rax
0075D595  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
0075D59A  48 C1 E3 0C                     shl rbx, 0xc
0075D59E  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
0075D5A3  48 8B CB                        mov rcx, rbx
0075D5A6  E8 65 2E 33 00                  call 0x140a90410
0075D5AB  44 8B C8                        mov r9d, eax
0075D5AE  85 C0                           test eax, eax
0075D5B0  78 35                           js 0x14075d5e7
0075D5B2  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0075D5B7  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0075D5BC  4C 89 05 15 08 7B 00            mov qword ptr [rip + 0x7b0815], r8
0075D5C3  48 89 0D 16 08 7B 00            mov qword ptr [rip + 0x7b0816], rcx
0075D5CA  48 89 1D FF 07 7B 00            mov qword ptr [rip + 0x7b07ff], rbx
0075D5D1  48 85 FF                        test rdi, rdi
0075D5D4  74 11                           je 0x14075d5e7
0075D5D6  48 6B C3 64                     imul rax, rbx, 0x64
0075D5DA  33 D2                           xor edx, edx
0075D5DC  49 F7 F0                        div r8
0075D5DF  83 F8 28                        cmp eax, 0x28
0075D5E2  0F 92 C0                        setb al
0075D5E5  88 07                           mov byte ptr [rdi], al
0075D5E7  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0075D5EC  41 8B C1                        mov eax, r9d
0075D5EF  48 83 C4 20                     add rsp, 0x20
0075D5F3  5F                              pop rdi
0075D5F4  C3                              ret
0075D5F5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEnlargeHiberFile(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 8063035) = *(unsigned __int64 *)(v_rip + 8055227);
    result = MmGetNumberOfPhysicalPages(a1, a2, a3, a4);
    v_rbx = (result) << (12);
    result = PopResizeHiberFile(v_rbx, v_stack_p10, v_stack_p18, a4);
    if (sign_flag) goto loc_0075D5E7;
    *(unsigned __int64 *)(v_rip + 8062997) = v_stack_p10;
    *(unsigned __int64 *)(v_rip + 8062998) = v_stack_p18;
    *(unsigned __int64 *)(v_rip + 8062975) = v_rbx;
    if (0 != 0) {
        result = (result) * (v_rbx);
        a2 = 0;
        result = (((unsigned int)(result)) < 40) ? 1 : 0;
        *(unsigned __int8 *)(a1) = (unsigned __int8)(result);
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t PopEnlargeHiberFile(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x7B083B) = *(uint64_t *)(v_rip + 0x7AE9BB);
    result = MmGetNumberOfPhysicalPages(Arg1, a2, a3, a4);
    local_rbx = (result) << (12);
    result = PopResizeHiberFile(local_rbx, v_stack_p10, v_stack_p18, a4);
    if (sign_flag) goto loc_0075D5E7;
    *(uint64_t *)(v_rip + 0x7B0815) = v_stack_p10;
    *(uint64_t *)(v_rip + 0x7B0816) = v_stack_p18;
    *(uint64_t *)(v_rip + 0x7B07FF) = local_rbx;
    if (0 != 0) {
        result = (result) * (local_rbx);
        a2 = 0;
        result = (((uint32_t)(result)) < 40) ? 1 : 0;
        *(uint8_t *)(Arg1) = (uint8_t)(result);
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0075D564&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0075D564[BB_0075D564]
  bb_0075D5B2[BB_0075D5B2]
  bb_0075D5D6[BB_0075D5D6]
  bb_0075D5E7[BB_0075D5E7]
  bb_0075D5F5[BB_0075D5F5]
  bb_0075D564 -->|branch| bb_0075D5E7
  bb_0075D564 -->|fallthrough| bb_0075D5B2
  bb_0075D5B2 -->|branch| bb_0075D5E7
  bb_0075D5B2 -->|fallthrough| bb_0075D5D6
  bb_0075D5D6 -->|flow| bb_0075D5E7
```
