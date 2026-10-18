# KsepDsEventRequestPowerIrp

- RVA: `0x005CD298`–`0x005CD399` (길이 `257` bytes)
- VA: `0x00000001405CD298`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB570`
- 디코드: `61`개 명령, `257/257` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CD2DC` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CD37E` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CD38A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseDsHookPoRequestPowerIrp](KseDsHookPoRequestPowerIrp_function_005CC5C0.md) at `0x005CC621`

### Static image references
- `0x005CD2B7` → RVA `0x00E0A740` (`.data`; read)
- `0x005CD2C5` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CD2D5` → RVA `0x00021648` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CD298  48 8B C4                        mov rax, rsp
005CD29B  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
005CD29F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
005CD2A3  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005CD2A7  48 89 48 08                     mov qword ptr [rax + 8], rcx
005CD2AB  55                              push rbp
005CD2AC  48 8D 68 B1                     lea rbp, [rax - 0x4f]
005CD2B0  48 81 EC B0 00 00 00            sub rsp, 0xb0
005CD2B7  48 8B 05 82 D4 83 00            mov rax, qword ptr [rip + 0x83d482]
005CD2BE  48 33 C4                        xor rax, rsp
005CD2C1  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
005CD2C5  48 8B 0D 14 9A 89 00            mov rcx, qword ptr [rip + 0x899a14]
005CD2CC  48 85 C9                        test rcx, rcx
005CD2CF  0F 84 AE 00 00 00               je 0x1405cd383
005CD2D5  48 8D 15 6C 43 A5 FF            lea rdx, [rip - 0x5abc94]
005CD2DC  E8 6F 51 DC FF                  call 0x140392450
005CD2E1  84 C0                           test al, al
005CD2E3  0F 84 9A 00 00 00               je 0x1405cd383
005CD2E9  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
005CD2ED  48 8D 45 57                     lea rax, [rbp + 0x57]
005CD2F1  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
005CD2F5  48 8D 15 4C 43 A5 FF            lea rdx, [rip - 0x5abcb4]
005CD2FC  83 65 03 00                     and dword ptr [rbp + 3], 0
005CD300  B9 08 00 00 00                  mov ecx, 8
005CD305  83 65 13 00                     and dword ptr [rbp + 0x13], 0
005CD309  45 33 C9                        xor r9d, r9d
005CD30C  83 65 23 00                     and dword ptr [rbp + 0x23], 0
005CD310  45 33 C0                        xor r8d, r8d
005CD313  83 65 33 00                     and dword ptr [rbp + 0x33], 0
005CD317  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
005CD31B  48 8D 45 5F                     lea rax, [rbp + 0x5f]
005CD31F  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
005CD323  48 8D 45 67                     lea rax, [rbp + 0x67]
005CD327  48 89 45 F7                     mov qword ptr [rbp - 9], rax
005CD32B  48 8D 45 6F                     lea rax, [rbp + 0x6f]
005CD32F  48 89 45 07                     mov qword ptr [rbp + 7], rax
005CD333  48 8D 45 77                     lea rax, [rbp + 0x77]
005CD337  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
005CD33B  48 8D 45 7F                     lea rax, [rbp + 0x7f]
005CD33F  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
005CD342  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
005CD345  89 4D FF                        mov dword ptr [rbp - 1], ecx
005CD348  B9 04 00 00 00                  mov ecx, 4
005CD34D  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
005CD351  48 8D 45 D7                     lea rax, [rbp - 0x29]
005CD355  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CD35A  C7 44 24 30 06 00 00 00         mov dword ptr [rsp + 0x30], 6
005CD362  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CD368  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CD36E  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
005CD371  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
005CD374  89 4D 2F                        mov dword ptr [rbp + 0x2f], ecx
005CD377  48 8B 0D 62 99 89 00            mov rcx, qword ptr [rip + 0x899962]
005CD37E  E8 4D 1D C9 FF                  call 0x14025f0d0
005CD383  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
005CD387  48 33 CC                        xor rcx, rsp
005CD38A  E8 B1 F2 0D 00                  call 0x1406ac640
005CD38F  48 81 C4 B0 00 00 00            add rsp, 0xb0
005CD396  5D                              pop rbp
005CD397  C3                              ret
005CD398  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDsEventRequestPowerIrp(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 8639618)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 79 + 55) = result;
    if (*(unsigned __int64 *)(v_rip + 9017876) == 0) goto loc_005CD383;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9017876), v_rip - 5946516, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 79 + 87;
        a2 = v_rip - 5946548;
        a1 = 8;
        a4 = 0;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 79 - 41) = result;
        result = v_rsp - 79 + 95;
        *(unsigned __int64 *)(v_rsp - 79 - 25) = result;
        result = v_rsp - 79 + 103;
        *(unsigned __int64 *)(v_rsp - 79 - 9) = result;
        result = v_rsp - 79 + 111;
        *(unsigned __int64 *)(v_rsp - 79 + 7) = result;
        result = v_rsp - 79 + 119;
        *(unsigned __int64 *)(v_rsp - 79 + 23) = result;
        result = v_rsp - 79 + 127;
        *(unsigned int *)(v_rsp - 79 - 33) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 79 - 17) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 79 - 1) = (unsigned int)(a1);
        a1 = 4;
        *(unsigned __int64 *)(v_rsp - 79 + 39) = result;
        result = v_rsp - 79 - 41;
        v_stack_m80 = result;
        v_stack_m88 = 6;
        *(unsigned int *)(v_rsp - 79 + 15) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 79 + 31) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 79 + 47) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9017698);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 79 + 55)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDsEventRequestPowerIrp(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x83D482)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x4F + 0x37) = result;
    if (*(uint64_t *)(v_rip + 0x899A14) == 0) goto loc_005CD383;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x899A14), v_rip - 5946516, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 79 + 87;
        Arg2 = v_rip - 5946548;
        Arg1 = 8;
        Arg4 = 0;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x4F - 0x29) = result;
        result = local_rsp - 79 + 95;
        *(uint64_t *)(local_rsp - 0x4F - 0x19) = result;
        result = local_rsp - 79 + 103;
        *(uint64_t *)(local_rsp - 0x4F - 0x9) = result;
        result = local_rsp - 79 + 111;
        *(uint64_t *)(local_rsp - 0x4F + 0x7) = result;
        result = local_rsp - 79 + 119;
        *(uint64_t *)(local_rsp - 0x4F + 0x17) = result;
        result = local_rsp - 79 + 127;
        *(uint32_t *)(local_rsp - 0x4F - 0x21) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x4F - 0x11) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x4F - 0x1) = (uint32_t)(Arg1);
        Arg1 = 4;
        *(uint64_t *)(local_rsp - 0x4F + 0x27) = result;
        result = local_rsp - 79 - 41;
        v_stack_m80 = result;
        v_stack_m88 = 6;
        *(uint32_t *)(local_rsp - 0x4F + 0xF) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x4F + 0x1F) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x4F + 0x2F) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x899962);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x4F + 0x37)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CD298&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CD298[BB_005CD298]
  bb_005CD2D5[BB_005CD2D5]
  bb_005CD2E9[BB_005CD2E9]
  bb_005CD383[BB_005CD383]
  bb_005CD398[BB_005CD398]
  bb_005CD298 -->|branch| bb_005CD383
  bb_005CD298 -->|fallthrough| bb_005CD2D5
  bb_005CD2D5 -->|branch| bb_005CD383
  bb_005CD2D5 -->|fallthrough| bb_005CD2E9
  bb_005CD2E9 -->|flow| bb_005CD383
```
