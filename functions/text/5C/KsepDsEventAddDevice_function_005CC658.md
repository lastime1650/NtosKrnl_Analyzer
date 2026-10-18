# KsepDsEventAddDevice

- RVA: `0x005CC658`–`0x005CC779` (길이 `289` bytes)
- VA: `0x00000001405CC658`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB5A0`
- 디코드: `71`개 명령, `289/289` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CC69B` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CC75E` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CC76A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseDsCallbackHookAddDevice](KseDsCallbackHookAddDevice_function_005CBEB0.md) at `0x005CBF6D`

### Static image references
- `0x005CC676` → RVA `0x00E0A740` (`.data`; read)
- `0x005CC684` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CC694` → RVA `0x00020EC8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CC658  48 8B C4                        mov rax, rsp
005CC65B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
005CC65F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
005CC663  89 50 10                        mov dword ptr [rax + 0x10], edx
005CC666  48 89 48 08                     mov qword ptr [rax + 8], rcx
005CC66A  55                              push rbp
005CC66B  48 8D 68 B9                     lea rbp, [rax - 0x47]
005CC66F  48 81 EC C0 00 00 00            sub rsp, 0xc0
005CC676  48 8B 05 C3 E0 83 00            mov rax, qword ptr [rip + 0x83e0c3]
005CC67D  48 33 C4                        xor rax, rsp
005CC680  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
005CC684  48 8B 0D 55 A6 89 00            mov rcx, qword ptr [rip + 0x89a655]
005CC68B  48 85 C9                        test rcx, rcx
005CC68E  0F 84 CF 00 00 00               je 0x1405cc763
005CC694  48 8D 15 2D 48 A5 FF            lea rdx, [rip - 0x5ab7d3]
005CC69B  E8 B0 5D DC FF                  call 0x140392450
005CC6A0  84 C0                           test al, al
005CC6A2  0F 84 BB 00 00 00               je 0x1405cc763
005CC6A8  83 65 CB 00                     and dword ptr [rbp - 0x35], 0
005CC6AC  48 8D 45 4F                     lea rax, [rbp + 0x4f]
005CC6B0  83 65 DB 00                     and dword ptr [rbp - 0x25], 0
005CC6B4  BA 08 00 00 00                  mov edx, 8
005CC6B9  83 65 EB 00                     and dword ptr [rbp - 0x15], 0
005CC6BD  45 33 C9                        xor r9d, r9d
005CC6C0  83 65 FB 00                     and dword ptr [rbp - 5], 0
005CC6C4  45 33 C0                        xor r8d, r8d
005CC6C7  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
005CC6CB  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
005CC6CF  8D 4A FC                        lea ecx, [rdx - 4]
005CC6D2  83 65 2B 00                     and dword ptr [rbp + 0x2b], 0
005CC6D6  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
005CC6DA  48 8D 45 57                     lea rax, [rbp + 0x57]
005CC6DE  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
005CC6E2  48 8D 45 5F                     lea rax, [rbp + 0x5f]
005CC6E6  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
005CC6EA  48 8D 45 67                     lea rax, [rbp + 0x67]
005CC6EE  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
005CC6F2  48 8D 45 6F                     lea rax, [rbp + 0x6f]
005CC6F6  48 89 45 FF                     mov qword ptr [rbp - 1], rax
005CC6FA  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
005CC6FD  89 4D 07                        mov dword ptr [rbp + 7], ecx
005CC700  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
005CC704  89 55 C7                        mov dword ptr [rbp - 0x39], edx
005CC707  89 55 E7                        mov dword ptr [rbp - 0x19], edx
005CC70A  89 55 F7                        mov dword ptr [rbp - 9], edx
005CC70D  48 8D 15 B4 47 A5 FF            lea rdx, [rip - 0x5ab84c]
005CC714  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
005CC718  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
005CC71C  0F B7 01                        movzx eax, word ptr [rcx]
005CC71F  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
005CC723  83 C0 02                        add eax, 2
005CC726  89 45 17                        mov dword ptr [rbp + 0x17], eax
005CC729  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
005CC72D  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
005CC731  0F B7 01                        movzx eax, word ptr [rcx]
005CC734  48 8B 0D A5 A5 89 00            mov rcx, qword ptr [rip + 0x89a5a5]
005CC73B  83 C0 02                        add eax, 2
005CC73E  89 45 27                        mov dword ptr [rbp + 0x27], eax
005CC741  48 8D 45 BF                     lea rax, [rbp - 0x41]
005CC745  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CC74A  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
005CC752  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CC758  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CC75E  E8 6D 29 C9 FF                  call 0x14025f0d0
005CC763  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
005CC767  48 33 CC                        xor rcx, rsp
005CC76A  E8 D1 FE 0D 00                  call 0x1406ac640
005CC76F  48 81 C4 C0 00 00 00            add rsp, 0xc0
005CC776  5D                              pop rbp
005CC777  C3                              ret
005CC778  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDsEventAddDevice(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 8642755)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 71 + 47) = result;
    if (*(unsigned __int64 *)(v_rip + 9021013) == 0) goto loc_005CC763;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9021013), v_rip - 5945299, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 71 + 79;
        a2 = 8;
        a4 = 0;
        a3 = 0;
        a1 = a2 - 4;
        *(unsigned __int64 *)(v_rsp - 71 - 65) = result;
        result = v_rsp - 71 + 87;
        *(unsigned __int64 *)(v_rsp - 71 - 49) = result;
        result = v_rsp - 71 + 95;
        *(unsigned __int64 *)(v_rsp - 71 - 33) = result;
        result = v_rsp - 71 + 103;
        *(unsigned __int64 *)(v_rsp - 71 - 17) = result;
        result = v_rsp - 71 + 111;
        *(unsigned __int64 *)(v_rsp - 71 - 1) = result;
        *(unsigned int *)(v_rsp - 71 - 41) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 71 + 7) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rsp - 71 + 119);
        *(unsigned int *)(v_rsp - 71 - 57) = a2;
        *(unsigned int *)(v_rsp - 71 - 25) = a2;
        *(unsigned int *)(v_rsp - 71 - 9) = a2;
        a2 = v_rip - 5945420;
        result = *(unsigned __int64 *)(a1 + 8);
        *(unsigned __int64 *)(v_rsp - 71 + 15) = result;
        result = *(unsigned __int16 *)(a1);
        a1 = *(unsigned __int64 *)(v_rsp - 71 + 127);
        result = (unsigned int)((result) + (2));
        *(unsigned int *)(v_rsp - 71 + 23) = (unsigned int)(result);
        result = *(unsigned __int64 *)(a1 + 8);
        *(unsigned __int64 *)(v_rsp - 71 + 31) = result;
        result = *(unsigned __int16 *)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9020837);
        result = (unsigned int)((result) + (2));
        *(unsigned int *)(v_rsp - 71 + 39) = (unsigned int)(result);
        result = v_rsp - 71 - 65;
        v_stack_m90 = result;
        v_stack_m98 = 7;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 71 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDsEventAddDevice(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x83E0C3)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x47 + 0x2F) = result;
    if (*(uint64_t *)(v_rip + 0x89A655) == 0) goto loc_005CC763;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x89A655), v_rip - 5945299, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 71 + 79;
        Arg2 = 8;
        Arg4 = 0;
        Arg3 = 0;
        Arg1 = Arg2 - 4;
        *(uint64_t *)(local_rsp - 0x47 - 0x41) = result;
        result = local_rsp - 71 + 87;
        *(uint64_t *)(local_rsp - 0x47 - 0x31) = result;
        result = local_rsp - 71 + 95;
        *(uint64_t *)(local_rsp - 0x47 - 0x21) = result;
        result = local_rsp - 71 + 103;
        *(uint64_t *)(local_rsp - 0x47 - 0x11) = result;
        result = local_rsp - 71 + 111;
        *(uint64_t *)(local_rsp - 0x47 - 0x1) = result;
        *(uint32_t *)(local_rsp - 0x47 - 0x29) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x47 + 0x7) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(local_rsp - 0x47 + 0x77);
        *(uint32_t *)(local_rsp - 0x47 - 0x39) = Arg2;
        *(uint32_t *)(local_rsp - 0x47 - 0x19) = Arg2;
        *(uint32_t *)(local_rsp - 0x47 - 0x9) = Arg2;
        Arg2 = v_rip - 5945420;
        result = *(uint64_t *)(Arg1 + 0x8);
        *(uint64_t *)(local_rsp - 0x47 + 0xF) = result;
        result = *(uint16_t *)(Arg1);
        Arg1 = *(uint64_t *)(local_rsp - 0x47 + 0x7F);
        result = (uint32_t)((result) + (2));
        *(uint32_t *)(local_rsp - 0x47 + 0x17) = (uint32_t)(result);
        result = *(uint64_t *)(Arg1 + 0x8);
        *(uint64_t *)(local_rsp - 0x47 + 0x1F) = result;
        result = *(uint16_t *)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x89A5A5);
        result = (uint32_t)((result) + (2));
        *(uint32_t *)(local_rsp - 0x47 + 0x27) = (uint32_t)(result);
        result = local_rsp - 71 - 65;
        v_stack_m90 = result;
        v_stack_m98 = 7;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x47 + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CC658&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CC658[BB_005CC658]
  bb_005CC694[BB_005CC694]
  bb_005CC6A8[BB_005CC6A8]
  bb_005CC763[BB_005CC763]
  bb_005CC778[BB_005CC778]
  bb_005CC658 -->|branch| bb_005CC763
  bb_005CC658 -->|fallthrough| bb_005CC694
  bb_005CC694 -->|branch| bb_005CC763
  bb_005CC694 -->|fallthrough| bb_005CC6A8
  bb_005CC6A8 -->|flow| bb_005CC763
```
