# MiDeliverPicoExceptionForProbedPage

- RVA: `0x00673DE4`–`0x00673E7D` (길이 `153` bytes)
- VA: `0x0000000140673DE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7B68`
- 디코드: `35`개 명령, `153/153` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00673E15` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00673E4B` → [PsPicoDispatchException](../4B/PsPicoDispatchException_function_004B7610.md) (function, `0x004B7610`)
- `0x00673E66` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiFaultInProbeAddress](../40/MiFaultInProbeAddress_function_0040E108.md) at `0x0040E214`

### Static image references
- `0x00673DF1` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00673DE4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00673DE9  57                              push rdi
00673DEA  48 81 EC E0 00 00 00            sub rsp, 0xe0
00673DF1  48 8B 05 48 69 79 00            mov rax, qword ptr [rip + 0x796948]
00673DF8  48 33 C4                        xor rax, rsp
00673DFB  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00673E03  8B FA                           mov edi, edx
00673E05  48 8B D9                        mov rbx, rcx
00673E08  33 D2                           xor edx, edx
00673E0A  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00673E0F  41 B8 98 00 00 00               mov r8d, 0x98
00673E15  E8 26 2E 05 00                  call 0x1406c6c40
00673E1A  C7 44 24 30 05 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000005
00673E22  C7 44 24 48 02 00 00 00         mov dword ptr [rsp + 0x48], 2
00673E2A  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00673E2F  85 FF                           test edi, edi
00673E31  74 09                           je 0x140673e3c
00673E33  48 C7 44 24 50 01 00 00 00      mov qword ptr [rsp + 0x50], 1
00673E3C  45 33 C0                        xor r8d, r8d
00673E3F  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00673E44  33 D2                           xor edx, edx
00673E46  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00673E4B  E8 C0 37 E4 FF                  call 0x1404b7610
00673E50  F6 D8                           neg al
00673E52  1B C0                           sbb eax, eax
00673E54  F7 D0                           not eax
00673E56  25 05 00 00 C0                  and eax, 0xc0000005
00673E5B  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00673E63  48 33 CC                        xor rcx, rsp
00673E66  E8 D5 87 03 00                  call 0x1406ac640
00673E6B  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00673E73  48 81 C4 E0 00 00 00            add rsp, 0xe0
00673E7A  5F                              pop rdi
00673E7B  C3                              ret
00673E7C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeliverPicoExceptionForProbedPage(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mB8;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 7956808)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_mB8, a2, 152, a4);
    v_stack_mB8 = 0xC0000005ULL;
    v_stack_mA0 = 2;
    v_stack_m90 = a1;
    if ((unsigned int)((unsigned int)(a2)) != 0) {
        v_stack_m98 = 1;
    }
    a3 = 0;
    v_stack_mC8 = 0;
    a2 = 0;
    result = PsPicoDispatchException(v_stack_mB8, a2, a3, a4);
    result = (unsigned __int8)(-(result));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC0000005ULL));
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeliverPicoExceptionForProbedPage(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mB8;
    uint8_t v_stack_mC8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x796948)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_mB8, Arg2, 152, a4);
    v_stack_mB8 = 0xC0000005ULL;
    v_stack_mA0 = 2;
    v_stack_m90 = Arg1;
    if ((uint32_t)((uint32_t)(Arg2)) != 0) {
        v_stack_m98 = 1;
    }
    a3 = 0;
    v_stack_mC8 = 0;
    Arg2 = 0;
    result = PsPicoDispatchException(v_stack_mB8, Arg2, a3, a4);
    result = (uint8_t)(-(result));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC0000005ULL));
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (224);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00673DE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00673DE4[BB_00673DE4]
  bb_00673E33[BB_00673E33]
  bb_00673E3C[BB_00673E3C]
  bb_00673E7C[BB_00673E7C]
  bb_00673DE4 -->|branch| bb_00673E3C
  bb_00673DE4 -->|fallthrough| bb_00673E33
  bb_00673E33 -->|flow| bb_00673E3C
```
