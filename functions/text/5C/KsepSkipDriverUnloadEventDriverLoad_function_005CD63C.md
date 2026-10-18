# KsepSkipDriverUnloadEventDriverLoad

- RVA: `0x005CD63C`–`0x005CD73E` (길이 `258` bytes)
- VA: `0x00000001405CD63C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB5CC`
- 디코드: `60`개 명령, `258/258` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CD683` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CD71B` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CD727` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseSkipDriverUnloadHookDriverTargeted](KseSkipDriverUnloadHookDriverTargeted_function_005CD600.md) at `0x005CD60C`

### Static image references
- `0x005CD65B` → RVA `0x00E0A740` (`.data`; read)
- `0x005CD66C` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CD67C` → RVA `0x00022488` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CD63C  48 8B C4                        mov rax, rsp
005CD63F  48 89 58 08                     mov qword ptr [rax + 8], rbx
005CD643  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
005CD647  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
005CD64B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005CD64F  55                              push rbp
005CD650  48 8D 68 A9                     lea rbp, [rax - 0x57]
005CD654  48 81 EC A0 00 00 00            sub rsp, 0xa0
005CD65B  48 8B 05 DE D0 83 00            mov rax, qword ptr [rip + 0x83d0de]
005CD662  48 33 C4                        xor rax, rsp
005CD665  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
005CD669  48 8B D9                        mov rbx, rcx
005CD66C  48 8B 0D 6D 96 89 00            mov rcx, qword ptr [rip + 0x89966d]
005CD673  48 85 C9                        test rcx, rcx
005CD676  0F 84 A4 00 00 00               je 0x1405cd720
005CD67C  48 8D 15 05 4E A5 FF            lea rdx, [rip - 0x5ab1fb]
005CD683  E8 C8 4D DC FF                  call 0x140392450
005CD688  84 C0                           test al, al
005CD68A  0F 84 90 00 00 00               je 0x1405cd720
005CD690  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
005CD694  48 8D 15 ED 4D A5 FF            lea rdx, [rip - 0x5ab213]
005CD69B  83 65 FB 00                     and dword ptr [rbp - 5], 0
005CD69F  B9 04 00 00 00                  mov ecx, 4
005CD6A4  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
005CD6A8  45 33 C9                        xor r9d, r9d
005CD6AB  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
005CD6AF  45 33 C0                        xor r8d, r8d
005CD6B2  83 65 2B 00                     and dword ptr [rbp + 0x2b], 0
005CD6B6  83 65 3B 00                     and dword ptr [rbp + 0x3b], 0
005CD6BA  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
005CD6BE  0F B7 03                        movzx eax, word ptr [rbx]
005CD6C1  83 C0 02                        add eax, 2
005CD6C4  89 4D 17                        mov dword ptr [rbp + 0x17], ecx
005CD6C7  89 45 F7                        mov dword ptr [rbp - 9], eax
005CD6CA  48 8D 45 67                     lea rax, [rbp + 0x67]
005CD6CE  48 89 45 FF                     mov qword ptr [rbp - 1], rax
005CD6D2  48 8D 45 6F                     lea rax, [rbp + 0x6f]
005CD6D6  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
005CD6DA  48 8D 45 77                     lea rax, [rbp + 0x77]
005CD6DE  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
005CD6E2  48 8D 45 7F                     lea rax, [rbp + 0x7f]
005CD6E6  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
005CD6EA  48 8D 45 EF                     lea rax, [rbp - 0x11]
005CD6EE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CD6F3  C7 44 24 30 05 00 00 00         mov dword ptr [rsp + 0x30], 5
005CD6FB  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CD701  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CD707  89 4D 27                        mov dword ptr [rbp + 0x27], ecx
005CD70A  89 4D 37                        mov dword ptr [rbp + 0x37], ecx
005CD70D  48 8B 0D CC 95 89 00            mov rcx, qword ptr [rip + 0x8995cc]
005CD714  C7 45 07 08 00 00 00            mov dword ptr [rbp + 7], 8
005CD71B  E8 B0 19 C9 FF                  call 0x14025f0d0
005CD720  48 8B 4D 3F                     mov rcx, qword ptr [rbp + 0x3f]
005CD724  48 33 CC                        xor rcx, rsp
005CD727  E8 14 EF 0D 00                  call 0x1406ac640
005CD72C  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
005CD734  48 81 C4 A0 00 00 00            add rsp, 0xa0
005CD73B  5D                              pop rbp
005CD73C  C3                              ret
005CD73D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepSkipDriverUnloadEventDriverLoad(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8638686)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 87 + 63) = result;
    if (*(unsigned __int64 *)(v_rip + 9016941) == 0) goto loc_005CD720;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9016941), v_rip - 5943803, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(a1 + 8);
        a2 = v_rip - 5943827;
        a1 = 4;
        a4 = 0;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 87 - 17) = result;
        result = *(unsigned __int16 *)(a1);
        result = (unsigned int)((result) + (2));
        *(unsigned int *)(v_rsp - 87 + 23) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 87 - 9) = (unsigned int)(result);
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
        *(unsigned int *)(v_rsp - 87 + 39) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 87 + 55) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9016780);
        *(unsigned int *)(v_rsp - 87 + 7) = 8;
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
int64_t KsepSkipDriverUnloadEventDriverLoad(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x83D0DE)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x57 + 0x3F) = result;
    if (*(uint64_t *)(v_rip + 0x89966D) == 0) goto loc_005CD720;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x89966D), v_rip - 5943803, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(arg1 + 0x8);
        Arg2 = v_rip - 5943827;
        Arg1 = 4;
        Arg4 = 0;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x57 - 0x11) = result;
        result = *(uint16_t *)(arg1);
        result = (uint32_t)((result) + (2));
        *(uint32_t *)(local_rsp - 0x57 + 0x17) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x57 - 0x9) = (uint32_t)(result);
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
        *(uint32_t *)(local_rsp - 0x57 + 0x27) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x57 + 0x37) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x8995CC);
        *(uint32_t *)(local_rsp - 0x57 + 0x7) = 8;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x57 + 0x3F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CD63C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CD63C[BB_005CD63C]
  bb_005CD67C[BB_005CD67C]
  bb_005CD690[BB_005CD690]
  bb_005CD720[BB_005CD720]
  bb_005CD73D[BB_005CD73D]
  bb_005CD63C -->|branch| bb_005CD720
  bb_005CD63C -->|fallthrough| bb_005CD67C
  bb_005CD67C -->|branch| bb_005CD720
  bb_005CD67C -->|fallthrough| bb_005CD690
  bb_005CD690 -->|flow| bb_005CD720
```
