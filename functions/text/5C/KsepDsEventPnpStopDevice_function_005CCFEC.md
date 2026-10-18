# KsepDsEventPnpStopDevice

- RVA: `0x005CCFEC`–`0x005CD0C7` (길이 `219` bytes)
- VA: `0x00000001405CCFEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC734`
- 디코드: `53`개 명령, `219/219` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CD030` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CD0AC` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CD0B8` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseDsCompletionHookForStopDevice](KseDsCompletionHookForStopDevice_function_005CC360.md) at `0x005CC372`

### Static image references
- `0x005CD00B` → RVA `0x00E0A740` (`.data`; read)
- `0x005CD019` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CD029` → RVA `0x00020D20` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CCFEC  48 8B C4                        mov rax, rsp
005CCFEF  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
005CCFF3  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
005CCFF7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005CCFFB  48 89 48 08                     mov qword ptr [rax + 8], rcx
005CCFFF  55                              push rbp
005CD000  48 8D 68 A1                     lea rbp, [rax - 0x5f]
005CD004  48 81 EC 90 00 00 00            sub rsp, 0x90
005CD00B  48 8B 05 2E D7 83 00            mov rax, qword ptr [rip + 0x83d72e]
005CD012  48 33 C4                        xor rax, rsp
005CD015  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
005CD019  48 8B 0D C0 9C 89 00            mov rcx, qword ptr [rip + 0x899cc0]
005CD020  48 85 C9                        test rcx, rcx
005CD023  0F 84 88 00 00 00               je 0x1405cd0b1
005CD029  48 8D 15 F0 3C A5 FF            lea rdx, [rip - 0x5ac310]
005CD030  E8 1B 54 DC FF                  call 0x140392450
005CD035  84 C0                           test al, al
005CD037  74 78                           je 0x1405cd0b1
005CD039  83 65 13 00                     and dword ptr [rbp + 0x13], 0
005CD03D  48 8D 45 67                     lea rax, [rbp + 0x67]
005CD041  83 65 23 00                     and dword ptr [rbp + 0x23], 0
005CD045  48 8D 15 D4 3C A5 FF            lea rdx, [rip - 0x5ac32c]
005CD04C  83 65 33 00                     and dword ptr [rbp + 0x33], 0
005CD050  B9 08 00 00 00                  mov ecx, 8
005CD055  83 65 43 00                     and dword ptr [rbp + 0x43], 0
005CD059  45 33 C9                        xor r9d, r9d
005CD05C  48 89 45 07                     mov qword ptr [rbp + 7], rax
005CD060  45 33 C0                        xor r8d, r8d
005CD063  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
005CD066  48 8D 45 6F                     lea rax, [rbp + 0x6f]
005CD06A  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
005CD06E  48 8D 45 77                     lea rax, [rbp + 0x77]
005CD072  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
005CD076  48 8D 45 7F                     lea rax, [rbp + 0x7f]
005CD07A  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
005CD07D  89 4D 2F                        mov dword ptr [rbp + 0x2f], ecx
005CD080  B9 04 00 00 00                  mov ecx, 4
005CD085  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
005CD089  48 8D 45 07                     lea rax, [rbp + 7]
005CD08D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CD092  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
005CD096  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CD09C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CD0A2  89 4D 3F                        mov dword ptr [rbp + 0x3f], ecx
005CD0A5  48 8B 0D 34 9C 89 00            mov rcx, qword ptr [rip + 0x899c34]
005CD0AC  E8 1F 20 C9 FF                  call 0x14025f0d0
005CD0B1  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
005CD0B5  48 33 CC                        xor rcx, rsp
005CD0B8  E8 83 F5 0D 00                  call 0x1406ac640
005CD0BD  48 81 C4 90 00 00 00            add rsp, 0x90
005CD0C4  5D                              pop rbp
005CD0C5  C3                              ret
005CD0C6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDsEventPnpStopDevice(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 8640302)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if (*(unsigned __int64 *)(v_rip + 9018560) == 0) goto loc_005CD0B1;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9018560), v_rip - 5948176, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 95 + 103;
        a2 = v_rip - 5948204;
        a1 = 8;
        a4 = 0;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        a3 = 0;
        *(unsigned int *)(v_rsp - 95 + 15) = (unsigned int)(a1);
        result = v_rsp - 95 + 111;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 + 119;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 + 127;
        *(unsigned int *)(v_rsp - 95 + 31) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 95 + 47) = (unsigned int)(a1);
        a1 = 4;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 + 7;
        v_stack_m60 = result;
        v_stack_m68 = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 95 + 63) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9018420);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDsEventPnpStopDevice(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x83D72E)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if (*(uint64_t *)(v_rip + 0x899CC0) == 0) goto loc_005CD0B1;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x899CC0), v_rip - 5948176, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 95 + 103;
        Arg2 = v_rip - 5948204;
        Arg1 = 8;
        Arg4 = 0;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = (uint32_t)(Arg1);
        result = local_rsp - 95 + 111;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 + 119;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 + 127;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = (uint32_t)(Arg1);
        Arg1 = 4;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 + 7;
        v_stack_m60 = result;
        v_stack_m68 = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x899C34);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CCFEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CCFEC[BB_005CCFEC]
  bb_005CD029[BB_005CD029]
  bb_005CD039[BB_005CD039]
  bb_005CD0B1[BB_005CD0B1]
  bb_005CD0C6[BB_005CD0C6]
  bb_005CCFEC -->|branch| bb_005CD0B1
  bb_005CCFEC -->|fallthrough| bb_005CD029
  bb_005CD029 -->|branch| bb_005CD0B1
  bb_005CD029 -->|fallthrough| bb_005CD039
  bb_005CD039 -->|flow| bb_005CD0B1
```
