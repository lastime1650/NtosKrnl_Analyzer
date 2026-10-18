# EtwTraceDpcProfilingStack

- RVA: `0x0044F1CC`–`0x0044F253` (길이 `135` bytes)
- VA: `0x000000014044F1CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6BF4`
- 디코드: `31`개 명령, `135/135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0044F23B` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0044F248` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeAccumulateTicks](../39/KeAccumulateTicks_function_0039C140.md) at `0x0039C508`

### Static image references
- `0x0044F1DB` → RVA `0x00E0A740` (`.data`; read)
- `0x0044F1EA` → RVA `0x00EFF830` (`.data`; read)
- `0x0044F209` → RVA `0x000223F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044F1CC  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0044F1D0  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
0044F1D4  4C 8B DC                        mov r11, rsp
0044F1D7  48 83 EC 78                     sub rsp, 0x78
0044F1DB  48 8B 05 5E B5 9B 00            mov rax, qword ptr [rip + 0x9bb55e]
0044F1E2  48 33 C4                        xor rax, rsp
0044F1E5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0044F1EA  48 8B 0D 3F 06 AB 00            mov rcx, qword ptr [rip + 0xab063f]
0044F1F1  45 33 C0                        xor r8d, r8d
0044F1F4  48 85 C9                        test rcx, rcx
0044F1F7  74 47                           je 0x14044f240
0044F1F9  49 8D 43 08                     lea rax, [r11 + 8]
0044F1FD  49 C7 43 D0 04 00 00 00         mov qword ptr [r11 - 0x30], 4
0044F205  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
0044F209  48 8D 15 E0 31 BD FF            lea rdx, [rip - 0x42ce20]
0044F210  49 8D 43 10                     lea rax, [r11 + 0x10]
0044F214  49 C7 43 E0 04 00 00 00         mov qword ptr [r11 - 0x20], 4
0044F21C  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0044F220  45 33 C9                        xor r9d, r9d
0044F223  49 8D 43 C8                     lea rax, [r11 - 0x38]
0044F227  49 89 43 C0                     mov qword ptr [r11 - 0x40], rax
0044F22B  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0044F233  4D 89 43 B0                     mov qword ptr [r11 - 0x50], r8
0044F237  4D 89 43 A8                     mov qword ptr [r11 - 0x58], r8
0044F23B  E8 90 FE E0 FF                  call 0x14025f0d0
0044F240  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0044F245  48 33 CC                        xor rcx, rsp
0044F248  E8 F3 D3 25 00                  call 0x1406ac640
0044F24D  48 83 C4 78                     add rsp, 0x78
0044F251  C3                              ret
0044F252  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceDpcProfilingStack(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m48;
    unsigned int v_stack_p10;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 10204510)) ^ (v_rsp);
    v_stack_m18 = result;
    a3 = 0;
    if (*(unsigned __int64 *)(v_rip + 11208255) != 0) {
        result = v_rsp + 8;
        *(unsigned __int64 *)(v_rsp - 48) = 4;
        *(unsigned __int64 *)(v_rsp - 56) = result;
        a2 = v_rip - 4378144;
        result = v_rsp + 16;
        *(unsigned __int64 *)(v_rsp - 32) = 4;
        *(unsigned __int64 *)(v_rsp - 40) = result;
        a4 = 0;
        result = v_rsp - 56;
        *(unsigned __int64 *)(v_rsp - 64) = result;
        v_stack_m48 = 2;
        *(unsigned __int64 *)(v_rsp - 80) = 0;
        *(unsigned __int64 *)(v_rsp - 88) = 0;
        result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 11208255), a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceDpcProfilingStack(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m48;
    uint32_t v_stack_p10;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x9BB55E)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg3 = 0;
    if (*(uint64_t *)(v_rip + 0xAB063F) != 0) {
        result = local_rsp + 8;
        *(uint64_t *)(local_rsp - 0x30) = 4;
        *(uint64_t *)(local_rsp - 0x38) = result;
        Arg2 = v_rip - 4378144;
        result = local_rsp + 16;
        *(uint64_t *)(local_rsp - 0x20) = 4;
        *(uint64_t *)(local_rsp - 0x28) = result;
        Arg4 = 0;
        result = local_rsp - 56;
        *(uint64_t *)(local_rsp - 0x40) = result;
        v_stack_m48 = 2;
        *(uint64_t *)(local_rsp - 0x50) = 0;
        *(uint64_t *)(local_rsp - 0x58) = 0;
        result = EtwWriteEx(*(uint64_t *)(v_rip + 0xAB063F), Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044F1CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044F1CC[BB_0044F1CC]
  bb_0044F1F9[BB_0044F1F9]
  bb_0044F240[BB_0044F240]
  bb_0044F252[BB_0044F252]
  bb_0044F1CC -->|branch| bb_0044F240
  bb_0044F1CC -->|fallthrough| bb_0044F1F9
  bb_0044F1F9 -->|flow| bb_0044F240
```
