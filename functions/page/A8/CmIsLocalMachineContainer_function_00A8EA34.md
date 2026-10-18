# CmIsLocalMachineContainer

- RVA: `0x00A8EA34`–`0x00A8EADC` (길이 `168` bytes)
- VA: `0x0000000140A8EA34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B8AA0`
- 디코드: `40`개 명령, `168/168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A8EA93` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00A8EAA9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A8EAD0` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)

### Direct callers
- [_CmGetDeviceContainerMappedProperty](../8F/_CmGetDeviceContainerMappedProperty_function_008F6A38.md) at `0x008F6AE6`
- [sub_00B266CA](../B2/Unknown_function_00B266CA.md) at `0x00B26900`

### Static image references
- `0x00A8EA43` → RVA `0x00E0A740` (`.data`; read)
- `0x00A8EA87` → RVA `0x00AFFD10` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A8EAA9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A8EAD0` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8EA34  4C 8B DC                        mov r11, rsp
00A8EA37  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
00A8EA3B  57                              push rdi
00A8EA3C  48 81 EC B0 00 00 00            sub rsp, 0xb0
00A8EA43  48 8B 05 F6 BC 37 00            mov rax, qword ptr [rip + 0x37bcf6]
00A8EA4A  48 33 C4                        xor rax, rsp
00A8EA4D  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00A8EA55  33 DB                           xor ebx, ebx
00A8EA57  C7 44 24 40 4E 00 00 00         mov dword ptr [rsp + 0x40], 0x4e
00A8EA5F  49 8D 43 88                     lea rax, [r11 - 0x78]
00A8EA63  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00A8EA67  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A8EA6C  48 8B FA                        mov rdi, rdx
00A8EA6F  49 8D 43 98                     lea rax, [r11 - 0x68]
00A8EA73  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00A8EA77  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A8EA7C  44 8D 4B 25                     lea r9d, [rbx + 0x25]
00A8EA80  49 8D 43 8C                     lea rax, [r11 - 0x74]
00A8EA84  45 33 C0                        xor r8d, r8d
00A8EA87  48 8D 15 82 12 07 00            lea rdx, [rip + 0x71282]
00A8EA8E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A8EA93  E8 D8 ED E5 FF                  call 0x1408ed870
00A8EA98  85 C0                           test eax, eax
00A8EA9A  79 24                           jns 0x140a8eac0
00A8EA9C  8A C3                           mov al, bl
00A8EA9E  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00A8EAA6  48 33 CC                        xor rcx, rsp
00A8EAA9  E8 92 DB C1 FF                  call 0x1406ac640
00A8EAAE  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00A8EAB6  48 81 C4 B0 00 00 00            add rsp, 0xb0
00A8EABD  5F                              pop rdi
00A8EABE  C3                              ret
00A8EABF  CC                              int3
00A8EAC0  48 8B D7                        mov rdx, rdi
00A8EAC3  66 89 9C 24 9C 00 00 00         mov word ptr [rsp + 0x9c], bx
00A8EACB  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A8EAD0  E8 AB 15 A7 FF                  call 0x140500080
00A8EAD5  85 C0                           test eax, eax
00A8EAD7  0F 94 C3                        sete bl
00A8EADA  EB C0                           jmp 0x140a8ea9c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmIsLocalMachineContainer(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p50;
    unsigned __int16 v_stack_p9C;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 3652854)) ^ (v_rsp);
    v_stack_m18 = result;
    v_rbx = 0;
    v_stack_m78 = 78;
    v_stack_m80 = 0;
    v_stack_m88 = v_rsp - 120;
    v_stack_m74 = 0;
    v_stack_m90 = v_rsp - 104;
    a3 = 0;
    v_stack_m98 = v_rsp - 116;
    result = CmGetDeviceRegProp(a1, v_rip + 463490, a3, v_rbx + 37);
    if (!sign_flag) goto loc_00A8EAC0;
loc_00A8EA9C:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip + 463490, a3, v_rbx + 37);
    v_rsp = (v_rsp) + (176);
    return result;
loc_00A8EAC0:
    v_stack_p9C = (unsigned __int16)(v_stack_p18);
    result = wcsicmp(v_stack_p50, a2, a3, v_rbx + 37);
    v_rbx = ((unsigned int)(result) == 0) ? 1 : 0;
    goto loc_00A8EA9C;
}
```

## 5. (Beta) C Style

```c
int64_t CmIsLocalMachineContainer(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p18;
    uint64_t v_stack_p50;
    uint16_t v_stack_p9C;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x37BCF6)) ^ (local_rsp);
    v_stack_m18 = result;
    local_rbx = 0;
    v_stack_m78 = 78;
    v_stack_m80 = 0;
    v_stack_m88 = local_rsp - 120;
    v_stack_m74 = 0;
    v_stack_m90 = local_rsp - 104;
    Arg3 = 0;
    v_stack_m98 = local_rsp - 116;
    result = CmGetDeviceRegProp(Arg1, v_rip + 463490, Arg3, local_rbx + 37);
    if (!sign_flag) goto loc_00A8EAC0;
loc_00A8EA9C:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip + 463490, Arg3, local_rbx + 37);
    local_rsp = (local_rsp) + (176);
    return result;
loc_00A8EAC0:
    v_stack_p9C = (uint16_t)(v_stack_p18);
    result = wcsicmp(v_stack_p50, Arg2, Arg3, local_rbx + 37);
    local_rbx = ((uint32_t)(result) == 0) ? 1 : 0;
    goto loc_00A8EA9C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8EA34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8EA34[BB_00A8EA34]
  bb_00A8EA9C[BB_00A8EA9C]
  bb_00A8EABF[BB_00A8EABF]
  bb_00A8EAC0[BB_00A8EAC0]
  bb_00A8EA34 -->|branch| bb_00A8EAC0
  bb_00A8EA34 -->|fallthrough| bb_00A8EA9C
  bb_00A8EABF -->|flow| bb_00A8EAC0
  bb_00A8EAC0 -->|branch| bb_00A8EA9C
```
