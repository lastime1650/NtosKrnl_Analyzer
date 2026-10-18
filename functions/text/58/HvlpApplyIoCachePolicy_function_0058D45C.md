# HvlpApplyIoCachePolicy

- RVA: `0x0058D45C`–`0x0058D4FC` (길이 `160` bytes)
- VA: `0x000000014058D45C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AF554`
- 디코드: `37`개 명령, `160/160` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0058D4A4` → [HvlpAcquireHypercallPage](../47/HvlpAcquireHypercallPage_function_00471410.md) (function, `0x00471410`)
- `0x0058D4C6` → [HvcallInitiateHypercall](../31/HvcallInitiateHypercall_function_00313630.md) (function, `0x00313630`)
- `0x0058D4D3` → [HvlpReleaseHypercallPage](../31/HvlpReleaseHypercallPage_function_00313480.md) (function, `0x00313480`)
- `0x0058D4ED` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HvlStartBootLogicalProcessors](HvlStartBootLogicalProcessors_function_00584E18.md) at `0x005851A1`

### Static image references
- `0x0058D465` → RVA `0x00E0A740` (`.data`; read)
- `0x0058D47C` → RVA `0x00F8EC98` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058D45C  40 53                           push rbx
0058D45E  48 81 EC A0 00 00 00            sub rsp, 0xa0
0058D465  48 8B 05 D4 D2 87 00            mov rax, qword ptr [rip + 0x87d2d4]
0058D46C  48 33 C4                        xor rax, rsp
0058D46F  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0058D477  33 C0                           xor eax, eax
0058D479  0F 57 C0                        xorps xmm0, xmm0
0058D47C  48 39 05 15 18 A0 00            cmp qword ptr [rip + 0xa01815], rax
0058D483  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0058D488  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0058D48D  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0058D491  74 4F                           je 0x14058d4e2
0058D493  44 8D 48 28                     lea r9d, [rax + 0x28]
0058D497  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
0058D49C  8D 50 01                        lea edx, [rax + 1]
0058D49F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0058D4A4  E8 67 3F EE FF                  call 0x140471410
0058D4A9  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0058D4AE  45 33 C0                        xor r8d, r8d
0058D4B1  C7 00 31 00 00 00               mov dword ptr [rax], 0x31
0058D4B7  48 8B 0D DA 17 A0 00            mov rcx, qword ptr [rip + 0xa017da]
0058D4BE  48 89 48 08                     mov qword ptr [rax + 8], rcx
0058D4C2  41 8D 48 6F                     lea ecx, [r8 + 0x6f]
0058D4C6  E8 65 61 D8 FF                  call 0x140313630
0058D4CB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0058D4D0  48 8B D8                        mov rbx, rax
0058D4D3  E8 A8 5F D8 FF                  call 0x140313480
0058D4D8  66 F7 DB                        neg bx
0058D4DB  1B C0                           sbb eax, eax
0058D4DD  25 01 00 00 C0                  and eax, 0xc0000001
0058D4E2  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0058D4EA  48 33 CC                        xor rcx, rsp
0058D4ED  E8 4E F1 11 00                  call 0x1406ac640
0058D4F2  48 81 C4 A0 00 00 00            add rsp, 0xa0
0058D4F9  5B                              pop rbx
0058D4FA  C3                              ret
0058D4FB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpApplyIoCachePolicy(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8901332)) ^ (v_rsp);
    v_stack_m18 = result;
    result = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    if ((*(unsigned __int64 *)(v_rip + 10491925)) != 0) {
        a4 = result + 40;
        a3 = v_stack_m68;
        a2 = result + 1;
        a1 = v_stack_m88;
        result = HvlpAcquireHypercallPage(a1, a2, a3, a4);
        a2 = v_stack_m70;
        a3 = 0;
        *(unsigned int *)(result) = 49;
        a1 = *(unsigned __int64 *)(v_rip + 10491866);
        *(unsigned __int64 *)(result + 8) = a1;
        a1 = a3 + 111;
        result = HvcallInitiateHypercall(a1, a2, a3, a4);
        a1 = v_stack_m88;
        v_rbx = result;
        result = HvlpReleaseHypercallPage(a1, a2, a3, a4);
        v_rbx = (unsigned __int16)(-(v_rbx));
        result = (unsigned int)((result) & (0xC0000001ULL));
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
void HvlpApplyIoCachePolicy(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x87D2D4)) ^ (local_rsp);
    v_stack_m18 = result;
    result = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    if ((*(uint64_t *)(v_rip + 0xA01815)) != 0) {
        a4 = result + 40;
        a3 = v_stack_m68;
        a2 = result + 1;
        a1 = v_stack_m88;
        result = HvlpAcquireHypercallPage(a1, a2, a3, a4);
        a2 = v_stack_m70;
        a3 = 0;
        *(uint32_t *)(result) = 49;
        a1 = *(uint64_t *)(v_rip + 0xA017DA);
        *(uint64_t *)(result + 0x8) = a1;
        a1 = a3 + 111;
        result = HvcallInitiateHypercall(a1, a2, a3, a4);
        a1 = v_stack_m88;
        local_rbx = result;
        result = HvlpReleaseHypercallPage(a1, a2, a3, a4);
        local_rbx = (uint16_t)(-(local_rbx));
        result = (uint32_t)((result) & (0xC0000001ULL));
    }
    a1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058D45C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058D45C[BB_0058D45C]
  bb_0058D493[BB_0058D493]
  bb_0058D4E2[BB_0058D4E2]
  bb_0058D4FB[BB_0058D4FB]
  bb_0058D45C -->|branch| bb_0058D4E2
  bb_0058D45C -->|fallthrough| bb_0058D493
  bb_0058D493 -->|flow| bb_0058D4E2
```
