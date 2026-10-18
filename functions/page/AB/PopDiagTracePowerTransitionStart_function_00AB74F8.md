# PopDiagTracePowerTransitionStart

- RVA: `0x00AB74F8`–`0x00AB75A0` (길이 `168` bytes)
- VA: `0x0000000140AB74F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCFCC`
- 디코드: `37`개 명령, `168/168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00AB7585` → [EtwWriteStartScenario](EtwWriteStartScenario_function_00AB75B0.md) (function, `0x00AB75B0`)
- `0x00AB7591` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopIssueActionRequest](../A9/PopIssueActionRequest_function_00A9CE54.md) at `0x00A9D075`

### Static image references
- `0x00AB7507` → RVA `0x00E0A740` (`.data`; read)
- `0x00AB7517` → RVA `0x00E67858` (`.data`; read)
- `0x00AB7530` → RVA `0x00E67870` (`.data`; read)
- `0x00AB7537` → RVA `0x0001E278` (`.rdata`; read)
- `0x00AB7541` → RVA `0x00F0B408` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AB7591` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB74F8  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00AB74FC  55                              push rbp
00AB74FD  48 8B EC                        mov rbp, rsp
00AB7500  48 81 EC 80 00 00 00            sub rsp, 0x80
00AB7507  48 8B 05 32 32 35 00            mov rax, qword ptr [rip + 0x353232]
00AB750E  48 33 C4                        xor rax, rsp
00AB7511  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00AB7515  33 D2                           xor edx, edx
00AB7517  38 15 3B 03 3B 00               cmp byte ptr [rip + 0x3b033b], dl
00AB751D  74 6B                           je 0x140ab758a
00AB751F  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
00AB7522  44 8D 4A 03                     lea r9d, [rdx + 3]
00AB7526  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00AB7530  4C 8D 05 39 03 3B 00            lea r8, [rip + 0x3b0339]
00AB7537  48 8D 15 3A 6D 56 FF            lea rdx, [rip - 0xa992c6]
00AB753E  48 8B 00                        mov rax, qword ptr [rax]
00AB7541  48 8B 0D C0 3E 45 00            mov rcx, qword ptr [rip + 0x453ec0]
00AB7548  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00AB754C  48 8D 45 B0                     lea rax, [rbp - 0x50]
00AB7550  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00AB7554  48 8D 45 18                     lea rax, [rbp + 0x18]
00AB7558  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00AB755C  48 8D 45 B8                     lea rax, [rbp - 0x48]
00AB7560  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00AB7564  48 8D 45 C0                     lea rax, [rbp - 0x40]
00AB7568  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB756D  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
00AB7575  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
00AB757D  48 C7 45 E8 08 00 00 00         mov qword ptr [rbp - 0x18], 8
00AB7585  E8 26 00 00 00                  call 0x140ab75b0
00AB758A  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00AB758E  48 33 CC                        xor rcx, rsp
00AB7591  E8 AA 50 BF FF                  call 0x1406ac640
00AB7596  48 81 C4 80 00 00 00            add rsp, 0x80
00AB759D  5D                              pop rbp
00AB759E  C3                              ret
00AB759F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTracePowerTransitionStart(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 3486258)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    if ((*(unsigned __int8 *)(v_rip + 3867451)) != 0) {
        v_stack_m58 = a1;
        a4 = a2 + 3;
        a3 = v_rip + 3867449;
        a2 = v_rip - 11113158;
        result = *(unsigned __int64 *)(result);
        a1 = *(unsigned __int64 *)(v_rip + 4538048);
        v_stack_m50 = result;
        result = v_stack_m58;
        v_stack_m48 = result;
        result = v_stack_p10;
        v_stack_m38 = result;
        result = v_stack_m50;
        v_stack_m28 = result;
        result = v_stack_m48;
        v_stack_m68 = result;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_m20 = 8;
        result = EtwWriteStartScenario(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTracePowerTransitionStart(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x353232)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    if ((*(uint8_t *)(v_rip + 0x3B033B)) != 0) {
        v_stack_m58 = Arg1;
        a4 = Arg2 + 3;
        a3 = v_rip + 3867449;
        Arg2 = v_rip - 11113158;
        result = *(uint64_t *)(result);
        Arg1 = *(uint64_t *)(v_rip + 0x453EC0);
        v_stack_m50 = result;
        result = v_stack_m58;
        v_stack_m48 = result;
        result = v_stack_p10;
        v_stack_m38 = result;
        result = v_stack_m50;
        v_stack_m28 = result;
        result = v_stack_m48;
        v_stack_m68 = result;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_m20 = 8;
        result = EtwWriteStartScenario(Arg1, Arg2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB74F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB74F8[BB_00AB74F8]
  bb_00AB751F[BB_00AB751F]
  bb_00AB758A[BB_00AB758A]
  bb_00AB759F[BB_00AB759F]
  bb_00AB74F8 -->|branch| bb_00AB758A
  bb_00AB74F8 -->|fallthrough| bb_00AB751F
  bb_00AB751F -->|flow| bb_00AB758A
```
