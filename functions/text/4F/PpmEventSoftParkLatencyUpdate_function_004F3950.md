# PpmEventSoftParkLatencyUpdate

- RVA: `0x004F3950`–`0x004F3A2E` (길이 `222` bytes)
- VA: `0x00000001404F3950`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9574`
- 디코드: `50`개 명령, `222/222` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x004F399C` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004F3A0D` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004F3A1A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkApplyPolicy](../4B/PpmParkApplyPolicy_function_004B613C.md) at `0x004B67B3`
- [PpmParkApplyPolicyEx](PpmParkApplyPolicyEx_function_004F3090.md) at `0x004F3880`
- [PpmEventTraceControlCallback](../../page/A5/PpmEventTraceControlCallback_function_00A51F60.md) at `0x00A520F1`

### Static image references
- `0x004F395F` → RVA `0x00E0A740` (`.data`; read)
- `0x004F3970` → RVA `0x0001C298` (`.rdata`; read)
- `0x004F3977` → RVA `0x0001C288` (`.rdata`; read)
- `0x004F3985` → RVA `0x00E67A39` (`.data`; read)
- `0x004F3992` → RVA `0x00F083E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F3950  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004F3955  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
004F395A  57                              push rdi
004F395B  48 83 EC 70                     sub rsp, 0x70
004F395F  48 8B 05 DA 6D 91 00            mov rax, qword ptr [rip + 0x916dda]
004F3966  48 33 C4                        xor rax, rsp
004F3969  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004F396E  84 C9                           test cl, cl
004F3970  48 8D 05 21 89 B2 FF            lea rax, [rip - 0x4d76df]
004F3977  48 8D 1D 0A 89 B2 FF            lea rbx, [rip - 0x4d76f6]
004F397E  40 8A FA                        mov dil, dl
004F3981  48 0F 44 D8                     cmove rbx, rax
004F3985  80 3D AD 40 97 00 00            cmp byte ptr [rip + 0x9740ad], 0
004F398C  0F 84 80 00 00 00               je 0x1404f3a12
004F3992  48 8B 0D 4F 4A A1 00            mov rcx, qword ptr [rip + 0xa14a4f]
004F3999  48 8B D3                        mov rdx, rbx
004F399C  E8 AF EA E9 FF                  call 0x140392450
004F39A1  84 C0                           test al, al
004F39A3  74 6D                           je 0x1404f3a12
004F39A5  33 C0                           xor eax, eax
004F39A7  B9 04 00 00 00                  mov ecx, 4
004F39AC  40 84 FF                        test dil, dil
004F39AF  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
004F39B3  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
004F39B7  48 8B D3                        mov rdx, rbx
004F39BA  48 8B 0D 27 4A A1 00            mov rcx, qword ptr [rip + 0xa14a27]
004F39C1  0F 95 C0                        setne al
004F39C4  83 64 24 54 00                  and dword ptr [rsp + 0x54], 0
004F39C9  45 33 C9                        xor r9d, r9d
004F39CC  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
004F39D1  45 33 C0                        xor r8d, r8d
004F39D4  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
004F39D8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004F39DD  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004F39E2  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
004F39EA  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004F39EF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
004F39F4  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004F39F9  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
004F3A01  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
004F3A07  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004F3A0D  E8 BE B6 D6 FF                  call 0x14025f0d0
004F3A12  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004F3A17  48 33 CC                        xor rcx, rsp
004F3A1A  E8 21 8C 1B 00                  call 0x1406ac640
004F3A1F  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
004F3A27  48 83 C4 70                     add rsp, 0x70
004F3A2B  5F                              pop rdi
004F3A2C  C3                              ret
004F3A2D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventSoftParkLatencyUpdate(unsigned __int8 a1, unsigned __int8 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 9530842)) ^ (v_rsp);
    v_stack_m10 = result;
    v_rbx = v_rip - 5076726;
    if (a1 == 0) { v_rbx = v_rip - 5076703; }
    if ((*(unsigned __int8 *)(v_rip + 9912493)) == 0) goto loc_004F3A12;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10570319), v_rbx, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = 0;
        a1 = 4;
        v_stack_m28 = a1;
        v_stack_m18 = a1;
        a2 = v_rbx;
        a1 = *(unsigned __int64 *)(v_rip + 10570279);
        result = (a2 != 0) ? 1 : 0;
        a4 = 0;
        a3 = 0;
        v_stack_m38 = (unsigned int)(result);
        result = v_stack_m38;
        v_stack_m30 = result;
        result = v_stack_p18;
        v_stack_m20 = result;
        result = v_stack_m30;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventSoftParkLatencyUpdate(uint8_t Arg1, uint8_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x916DDA)) ^ (local_rsp);
    v_stack_m10 = result;
    local_rbx = v_rip - 5076726;
    if (Arg1 == 0) { local_rbx = v_rip - 5076703; }
    if ((*(uint8_t *)(v_rip + 0x9740AD)) == 0) goto loc_004F3A12;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA14A4F), local_rbx, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = 0;
        Arg1 = 4;
        v_stack_m28 = Arg1;
        v_stack_m18 = Arg1;
        Arg2 = local_rbx;
        Arg1 = *(uint64_t *)(v_rip + 0xA14A27);
        result = (Arg2 != 0) ? 1 : 0;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_m38 = (uint32_t)(result);
        result = v_stack_m38;
        v_stack_m30 = result;
        result = v_stack_p18;
        v_stack_m20 = result;
        result = v_stack_m30;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (112);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F3950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F3950[BB_004F3950]
  bb_004F3992[BB_004F3992]
  bb_004F39A5[BB_004F39A5]
  bb_004F3A12[BB_004F3A12]
  bb_004F3A2D[BB_004F3A2D]
  bb_004F3950 -->|branch| bb_004F3A12
  bb_004F3950 -->|fallthrough| bb_004F3992
  bb_004F3992 -->|branch| bb_004F3A12
  bb_004F3992 -->|fallthrough| bb_004F39A5
  bb_004F39A5 -->|flow| bb_004F3A12
```
