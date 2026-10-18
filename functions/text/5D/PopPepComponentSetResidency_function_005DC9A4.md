# PopPepComponentSetResidency

- RVA: `0x005DC9A4`–`0x005DCA99` (길이 `245` bytes)
- VA: `0x00000001405DC9A4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9EA4`
- 디코드: `67`개 명령, `245/245` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005DC9E0` → [PopPepComponentGetResidencyIdleState](../45/PopPepComponentGetResidencyIdleState_function_00459038.md) (function, `0x00459038`)
- `0x005DCA02` → [PopPepLockActivityLink](../26/PopPepLockActivityLink_function_0026F7A0.md) (function, `0x0026F7A0`)
- `0x005DCA34` → [PopPepCountReadyActivities](../43/PopPepCountReadyActivities_function_0043E160.md) (function, `0x0043E160`)
- `0x005DCA44` → [PopPepUpdateIdleState](../2B/PopPepUpdateIdleState_function_002BF794.md) (function, `0x002BF794`)
- `0x005DCA52` → [PopPepPromoteActivities](../24/PopPepPromoteActivities_function_0024D0D0.md) (function, `0x0024D0D0`)
- `0x005DCA60` → [PopPepCountReadyActivities](../43/PopPepCountReadyActivities_function_0043E160.md) (function, `0x0043E160`)
- `0x005DCA6D` → [PopPepRequestWork](../39/PopPepRequestWork_function_003986F0.md) (function, `0x003986F0`)
- `0x005DCA80` → [PopPepReleaseActivityLink](../24/PopPepReleaseActivityLink_function_0024CC90.md) (function, `0x0024CC90`)

### Direct callers
- [PoFxSetComponentResidency](PoFxSetComponentResidency_function_005D2100.md) at `0x005D2129`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DC9A4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005DC9A9  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
005DC9AE  56                              push rsi
005DC9AF  57                              push rdi
005DC9B0  41 56                           push r14
005DC9B2  48 83 EC 30                     sub rsp, 0x30
005DC9B6  8B C2                           mov eax, edx
005DC9B8  48 8D B9 C0 00 00 00            lea rdi, [rcx + 0xc0]
005DC9BF  48 69 D0 D0 00 00 00            imul rdx, rax, 0xd0
005DC9C6  33 DB                           xor ebx, ebx
005DC9C8  48 8B F1                        mov rsi, rcx
005DC9CB  48 03 FA                        add rdi, rdx
005DC9CE  88 5C 24 58                     mov byte ptr [rsp + 0x58], bl
005DC9D2  49 83 F8 FF                     cmp r8, -1
005DC9D6  48 8B CF                        mov rcx, rdi
005DC9D9  49 0F 45 D8                     cmovne rbx, r8
005DC9DD  48 8B D3                        mov rdx, rbx
005DC9E0  E8 53 C6 E7 FF                  call 0x140459038
005DC9E5  41 B9 01 00 00 00               mov r9d, 1
005DC9EB  44 8B F0                        mov r14d, eax
005DC9EE  48 8D 44 24 58                  lea rax, [rsp + 0x58]
005DC9F3  48 8B D7                        mov rdx, rdi
005DC9F6  48 8B CE                        mov rcx, rsi
005DC9F9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005DC9FE  45 8D 41 05                     lea r8d, [r9 + 5]
005DCA02  E8 99 2D C9 FF                  call 0x14026f7a0
005DCA07  48 89 9F 80 00 00 00            mov qword ptr [rdi + 0x80], rbx
005DCA0E  40 8A E8                        mov bpl, al
005DCA11  48 89 5F 78                     mov qword ptr [rdi + 0x78], rbx
005DCA15  44 39 B7 A0 00 00 00            cmp dword ptr [rdi + 0xa0], r14d
005DCA1C  74 54                           je 0x1405dca72
005DCA1E  44 89 B7 A0 00 00 00            mov dword ptr [rdi + 0xa0], r14d
005DCA25  48 8B D7                        mov rdx, rdi
005DCA28  41 BE 02 00 00 00               mov r14d, 2
005DCA2E  48 8B CE                        mov rcx, rsi
005DCA31  45 8B C6                        mov r8d, r14d
005DCA34  E8 27 17 E6 FF                  call 0x14043e160
005DCA39  41 B0 01                        mov r8b, 1
005DCA3C  48 8B D7                        mov rdx, rdi
005DCA3F  48 8B CE                        mov rcx, rsi
005DCA42  8B D8                           mov ebx, eax
005DCA44  E8 4B 2D CE FF                  call 0x1402bf794
005DCA49  45 8B C6                        mov r8d, r14d
005DCA4C  48 8B D7                        mov rdx, rdi
005DCA4F  48 8B CE                        mov rcx, rsi
005DCA52  E8 79 06 C7 FF                  call 0x14024d0d0
005DCA57  45 8B C6                        mov r8d, r14d
005DCA5A  48 8B D7                        mov rdx, rdi
005DCA5D  48 8B CE                        mov rcx, rsi
005DCA60  E8 FB 16 E6 FF                  call 0x14043e160
005DCA65  44 8B C0                        mov r8d, eax
005DCA68  8B D3                           mov edx, ebx
005DCA6A  48 8B CE                        mov rcx, rsi
005DCA6D  E8 7E BC DB FF                  call 0x1403986f0
005DCA72  44 8A 4C 24 58                  mov r9b, byte ptr [rsp + 0x58]
005DCA77  44 8A C5                        mov r8b, bpl
005DCA7A  48 8B D7                        mov rdx, rdi
005DCA7D  48 8B CE                        mov rcx, rsi
005DCA80  E8 0B 02 C7 FF                  call 0x14024cc90
005DCA85  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
005DCA8A  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
005DCA8F  48 83 C4 30                     add rsp, 0x30
005DCA93  41 5E                           pop r14
005DCA95  5F                              pop rdi
005DCA96  5E                              pop rsi
005DCA97  C3                              ret
005DCA98  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPepComponentSetResidency(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (48);
    a2 = (a2) * ((unsigned int)(a2));
    v_rbx = 0;
    v_rdi = (a1 + 192) + (a2);
    v_stack_p10 = 0;
    if (a3 != -1) { v_rbx = a3; }
    result = PopPepComponentGetResidencyIdleState(v_rdi, v_rbx, a3, a4);
    v_stack_m28 = v_stack_p10;
    result = PopPepLockActivityLink(a1, v_rdi, 1 + 5, 1);
    *(unsigned __int64 *)(v_rdi + 128) = v_rbx;
    *(unsigned __int64 *)(v_rdi + 120) = v_rbx;
    v_r14 = (unsigned int)((unsigned int)(result));
    if ((*(unsigned int *)(v_rdi + 160)) != ((unsigned int)((unsigned int)((unsigned int)(result))))) {
        *(unsigned int *)(v_rdi + 160) = (unsigned int)((unsigned int)((unsigned int)(result)));
        a2 = v_rdi;
        v_r14 = 2;
        a1 = a1;
        a3 = (unsigned int)(v_r14);
        result = PopPepCountReadyActivities(a1, a2, a3, 1);
        a3 = 1;
        a2 = v_rdi;
        a1 = a1;
        v_rbx = (unsigned int)(result);
        result = PopPepUpdateIdleState(a1, a2, a3, 1);
        a3 = (unsigned int)(v_r14);
        a2 = v_rdi;
        a1 = a1;
        result = PopPepPromoteActivities(a1, a2, a3, 1);
        a3 = (unsigned int)(v_r14);
        a2 = v_rdi;
        a1 = a1;
        result = PopPepCountReadyActivities(a1, a2, a3, 1);
        a3 = (unsigned int)(result);
        a2 = (unsigned int)(v_rbx);
        a1 = a1;
        result = PopPepRequestWork(a1, a2, a3, 1);
    }
    result = PopPepReleaseActivityLink(a1, v_rdi, (unsigned __int8)((unsigned __int8)(result)), v_stack_p10);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPepComponentSetResidency(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (48);
    Arg2 = (Arg2) * ((uint32_t)(Arg2));
    local_rbx = 0;
    local_rdi = (Arg1 + 192) + (Arg2);
    v_stack_p10 = 0;
    if (Arg3 != -1) { local_rbx = Arg3; }
    result = PopPepComponentGetResidencyIdleState(local_rdi, local_rbx, Arg3, a4);
    v_stack_m28 = v_stack_p10;
    result = PopPepLockActivityLink(Arg1, local_rdi, 1 + 5, 1);
    *(uint64_t *)(local_rdi + 0x80) = local_rbx;
    *(uint64_t *)(local_rdi + 0x78) = local_rbx;
    local_r14 = (uint32_t)((uint32_t)(result));
    if ((*(uint32_t *)(local_rdi + 0xA0)) != ((uint32_t)((uint32_t)((uint32_t)(result))))) {
        *(uint32_t *)(local_rdi + 0xA0) = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg2 = local_rdi;
        local_r14 = 2;
        Arg1 = Arg1;
        Arg3 = (uint32_t)(local_r14);
        result = PopPepCountReadyActivities(Arg1, Arg2, Arg3, 1);
        Arg3 = 1;
        Arg2 = local_rdi;
        Arg1 = Arg1;
        local_rbx = (uint32_t)(result);
        result = PopPepUpdateIdleState(Arg1, Arg2, Arg3, 1);
        Arg3 = (uint32_t)(local_r14);
        Arg2 = local_rdi;
        Arg1 = Arg1;
        result = PopPepPromoteActivities(Arg1, Arg2, Arg3, 1);
        Arg3 = (uint32_t)(local_r14);
        Arg2 = local_rdi;
        Arg1 = Arg1;
        result = PopPepCountReadyActivities(Arg1, Arg2, Arg3, 1);
        Arg3 = (uint32_t)(result);
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = Arg1;
        result = PopPepRequestWork(Arg1, Arg2, Arg3, 1);
    }
    result = PopPepReleaseActivityLink(Arg1, local_rdi, (uint8_t)((uint8_t)(result)), v_stack_p10);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `64` | `W` |
| `Arg1` | `+ 0x80` | `64` | `W` |
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `W` |
| `Arg1` | `+ 0xC0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DC9A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DC9A4[BB_005DC9A4]
  bb_005DCA1E[BB_005DCA1E]
  bb_005DCA72[BB_005DCA72]
  bb_005DCA98[BB_005DCA98]
  bb_005DC9A4 -->|branch| bb_005DCA72
  bb_005DC9A4 -->|fallthrough| bb_005DCA1E
  bb_005DCA1E -->|flow| bb_005DCA72
```
