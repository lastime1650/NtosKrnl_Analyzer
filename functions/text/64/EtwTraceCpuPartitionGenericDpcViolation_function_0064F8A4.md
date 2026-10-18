# EtwTraceCpuPartitionGenericDpcViolation

- RVA: `0x0064F8A4`–`0x0064F939` (길이 `149` bytes)
- VA: `0x000000014064F8A4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEE48`
- 디코드: `32`개 명령, `149/149` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064F8CF` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0064F921` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0064F92E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiCpuPartitionCheckGenericDpc](../5C/KiCpuPartitionCheckGenericDpc_function_005C159C.md) at `0x005C15C2`

### Static image references
- `0x0064F8AD` → RVA `0x00E0A740` (`.data`; read)
- `0x0064F8BC` → RVA `0x00EFF858` (`.data`; read)
- `0x0064F8C8` → RVA `0x000223A0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064F8A4  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0064F8A9  48 83 EC 68                     sub rsp, 0x68
0064F8AD  48 8B 05 8C AE 7B 00            mov rax, qword ptr [rip + 0x7bae8c]
0064F8B4  48 33 C4                        xor rax, rsp
0064F8B7  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0064F8BC  48 8B 0D 95 FF 8A 00            mov rcx, qword ptr [rip + 0x8aff95]
0064F8C3  48 85 C9                        test rcx, rcx
0064F8C6  74 5E                           je 0x14064f926
0064F8C8  48 8D 15 D1 2A 9D FF            lea rdx, [rip - 0x62d52f]
0064F8CF  E8 7C 2B D4 FF                  call 0x140392450
0064F8D4  84 C0                           test al, al
0064F8D6  74 4E                           je 0x14064f926
0064F8D8  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
0064F8DD  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0064F8E2  48 8B 0D 6F FF 8A 00            mov rcx, qword ptr [rip + 0x8aff6f]
0064F8E9  48 8D 15 B0 2A 9D FF            lea rdx, [rip - 0x62d550]
0064F8F0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0064F8F5  45 33 C9                        xor r9d, r9d
0064F8F8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0064F8FD  C7 44 24 48 08 00 00 00         mov dword ptr [rsp + 0x48], 8
0064F905  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0064F90A  45 33 C0                        xor r8d, r8d
0064F90D  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
0064F915  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0064F91B  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0064F921  E8 AA F7 C0 FF                  call 0x14025f0d0
0064F926  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0064F92B  48 33 CC                        xor rcx, rsp
0064F92E  E8 0D CD 05 00                  call 0x1406ac640
0064F933  48 83 C4 68                     add rsp, 0x68
0064F937  C3                              ret
0064F938  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceCpuPartitionGenericDpcViolation(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 8105612)) ^ (v_rsp);
    v_stack_m18 = result;
    if (*(unsigned __int64 *)(v_rip + 9109397) == 0) goto loc_0064F926;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9109397), v_rip - 6477103, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 9109359);
        a2 = v_rip - 6477136;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m28;
        v_stack_m20 = 8;
        v_stack_m30 = result;
        a3 = 0;
        v_stack_m38 = 1;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceCpuPartitionGenericDpcViolation(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x7BAE8C)) ^ (local_rsp);
    v_stack_m18 = result;
    if (*(uint64_t *)(v_rip + 0x8AFF95) == 0) goto loc_0064F926;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x8AFF95), v_rip - 6477103, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x8AFF6F);
        Arg2 = v_rip - 6477136;
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m28;
        v_stack_m20 = 8;
        v_stack_m30 = result;
        Arg3 = 0;
        v_stack_m38 = 1;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064F8A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064F8A4[BB_0064F8A4]
  bb_0064F8C8[BB_0064F8C8]
  bb_0064F8D8[BB_0064F8D8]
  bb_0064F926[BB_0064F926]
  bb_0064F938[BB_0064F938]
  bb_0064F8A4 -->|branch| bb_0064F926
  bb_0064F8A4 -->|fallthrough| bb_0064F8C8
  bb_0064F8C8 -->|branch| bb_0064F926
  bb_0064F8C8 -->|fallthrough| bb_0064F8D8
  bb_0064F8D8 -->|flow| bb_0064F926
```
