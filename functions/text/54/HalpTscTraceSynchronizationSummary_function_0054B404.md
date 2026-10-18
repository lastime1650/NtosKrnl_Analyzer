# HalpTscTraceSynchronizationSummary

- RVA: `0x0054B404`–`0x0054B4F3` (길이 `239` bytes)
- VA: `0x000000014054B404`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6C08`
- 디코드: `56`개 명령, `239/239` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0054B44A` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0054B4D8` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0054B4E4` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HalpTscAdvSynchLeader](HalpTscAdvSynchLeader_function_0054A690.md) at `0x0054A848`

### Static image references
- `0x0054B421` → RVA `0x00E0A740` (`.data`; read)
- `0x0054B42F` → RVA `0x00FC22C0` (`.data`; read)
- `0x0054B43C` → RVA `0x00FC22B8` (`.data`; read)
- `0x0054B443` → RVA `0x000215F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054B404  48 8B C4                        mov rax, rsp
0054B407  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
0054B40B  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
0054B40F  89 50 10                        mov dword ptr [rax + 0x10], edx
0054B412  89 48 08                        mov dword ptr [rax + 8], ecx
0054B415  55                              push rbp
0054B416  48 8D 68 A9                     lea rbp, [rax - 0x57]
0054B41A  48 81 EC A0 00 00 00            sub rsp, 0xa0
0054B421  48 8B 05 18 F3 8B 00            mov rax, qword ptr [rip + 0x8bf318]
0054B428  48 33 C4                        xor rax, rsp
0054B42B  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
0054B42F  80 3D 8A 6E A7 00 00            cmp byte ptr [rip + 0xa76e8a], 0
0054B436  0F 84 A1 00 00 00               je 0x14054b4dd
0054B43C  48 8B 0D 75 6E A7 00            mov rcx, qword ptr [rip + 0xa76e75]
0054B443  48 8D 15 A6 61 AD FF            lea rdx, [rip - 0x529e5a]
0054B44A  E8 01 70 E4 FF                  call 0x140392450
0054B44F  84 C0                           test al, al
0054B451  0F 84 86 00 00 00               je 0x14054b4dd
0054B457  83 65 FB 00                     and dword ptr [rbp - 5], 0
0054B45B  48 8D 45 5F                     lea rax, [rbp + 0x5f]
0054B45F  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
0054B463  48 8D 15 86 61 AD FF            lea rdx, [rip - 0x529e7a]
0054B46A  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
0054B46E  B9 04 00 00 00                  mov ecx, 4
0054B473  83 65 2B 00                     and dword ptr [rbp + 0x2b], 0
0054B477  45 33 C9                        xor r9d, r9d
0054B47A  83 65 3B 00                     and dword ptr [rbp + 0x3b], 0
0054B47E  45 33 C0                        xor r8d, r8d
0054B481  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
0054B485  48 8D 45 67                     lea rax, [rbp + 0x67]
0054B489  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0054B48D  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0054B491  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
0054B495  48 8D 45 77                     lea rax, [rbp + 0x77]
0054B499  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
0054B49D  48 8D 45 7F                     lea rax, [rbp + 0x7f]
0054B4A1  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
0054B4A5  48 8D 45 EF                     lea rax, [rbp - 0x11]
0054B4A9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0054B4AE  C7 44 24 30 05 00 00 00         mov dword ptr [rsp + 0x30], 5
0054B4B6  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0054B4BC  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0054B4C2  89 4D F7                        mov dword ptr [rbp - 9], ecx
0054B4C5  89 4D 07                        mov dword ptr [rbp + 7], ecx
0054B4C8  89 4D 17                        mov dword ptr [rbp + 0x17], ecx
0054B4CB  89 4D 27                        mov dword ptr [rbp + 0x27], ecx
0054B4CE  89 4D 37                        mov dword ptr [rbp + 0x37], ecx
0054B4D1  48 8B 0D E0 6D A7 00            mov rcx, qword ptr [rip + 0xa76de0]
0054B4D8  E8 F3 3B D1 FF                  call 0x14025f0d0
0054B4DD  48 8B 4D 3F                     mov rcx, qword ptr [rbp + 0x3f]
0054B4E1  48 33 CC                        xor rcx, rsp
0054B4E4  E8 57 11 16 00                  call 0x1406ac640
0054B4E9  48 81 C4 A0 00 00 00            add rsp, 0xa0
0054B4F0  5D                              pop rbp
0054B4F1  C3                              ret
0054B4F2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTscTraceSynchronizationSummary(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 9171736)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 87 + 63) = result;
    if ((*(unsigned __int8 *)(v_rip + 10972810)) == 0) goto loc_0054B4DD;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10972789), v_rip - 5414490, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 87 + 95;
        a2 = v_rip - 5414522;
        a1 = 4;
        a4 = 0;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 87 - 17) = result;
        result = v_rsp - 87 + 103;
        *(unsigned __int64 *)(v_rsp - 87 - 1) = result;
        result = v_rsp - 87 + 111;
        *(unsigned __int64 *)(v_rsp - 87 + 15) = result;
        result = v_rsp - 87 + 119;
        *(unsigned __int64 *)(v_rsp - 87 + 31) = result;
        result = v_rsp - 87 + 127;
        *(unsigned __int64 *)(v_rsp - 87 + 47) = result;
        result = v_rsp - 87 - 17;
        v_stack_m70 = result;
        v_stack_m78 = 5;
        *(unsigned int *)(v_rsp - 87 - 9) = a1;
        *(unsigned int *)(v_rsp - 87 + 7) = a1;
        *(unsigned int *)(v_rsp - 87 + 23) = a1;
        *(unsigned int *)(v_rsp - 87 + 39) = a1;
        *(unsigned int *)(v_rsp - 87 + 55) = a1;
        a1 = *(unsigned __int64 *)(v_rip + 10972640);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 87 + 63)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpTscTraceSynchronizationSummary(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x8BF318)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x57 + 0x3F) = result;
    if ((*(uint8_t *)(v_rip + 0xA76E8A)) == 0) goto loc_0054B4DD;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA76E75), v_rip - 5414490, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 87 + 95;
        Arg2 = v_rip - 5414522;
        Arg1 = 4;
        Arg4 = 0;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x57 - 0x11) = result;
        result = local_rsp - 87 + 103;
        *(uint64_t *)(local_rsp - 0x57 - 0x1) = result;
        result = local_rsp - 87 + 111;
        *(uint64_t *)(local_rsp - 0x57 + 0xF) = result;
        result = local_rsp - 87 + 119;
        *(uint64_t *)(local_rsp - 0x57 + 0x1F) = result;
        result = local_rsp - 87 + 127;
        *(uint64_t *)(local_rsp - 0x57 + 0x2F) = result;
        result = local_rsp - 87 - 17;
        v_stack_m70 = result;
        v_stack_m78 = 5;
        *(uint32_t *)(local_rsp - 0x57 - 0x9) = Arg1;
        *(uint32_t *)(local_rsp - 0x57 + 0x7) = Arg1;
        *(uint32_t *)(local_rsp - 0x57 + 0x17) = Arg1;
        *(uint32_t *)(local_rsp - 0x57 + 0x27) = Arg1;
        *(uint32_t *)(local_rsp - 0x57 + 0x37) = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0xA76DE0);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x57 + 0x3F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054B404&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054B404[BB_0054B404]
  bb_0054B43C[BB_0054B43C]
  bb_0054B457[BB_0054B457]
  bb_0054B4DD[BB_0054B4DD]
  bb_0054B4F2[BB_0054B4F2]
  bb_0054B404 -->|branch| bb_0054B4DD
  bb_0054B404 -->|fallthrough| bb_0054B43C
  bb_0054B43C -->|branch| bb_0054B4DD
  bb_0054B43C -->|fallthrough| bb_0054B457
  bb_0054B457 -->|flow| bb_0054B4DD
```
