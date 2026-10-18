# PopEtStringIntern

- RVA: `0x0098E7D0`–`0x0098E84A` (길이 `122` bytes)
- VA: `0x000000014098E7D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009893C`
- 디코드: `31`개 명령, `122/122` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0098E828` → [RtlInternTableIntern](RtlInternTableIntern_function_0098EEB4.md) (function, `0x0098EEB4`)

### Direct callers
- [PopEtEnergyContextSetState](PopEtEnergyContextSetState_function_0098CF94.md) at `0x0098D05A`

### Static image references
- `0x0098E7E4` → RVA `0x00E67A30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098E7D0  4C 8B DC                        mov r11, rsp
0098E7D3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0098E7D7  57                              push rdi
0098E7D8  48 83 EC 60                     sub rsp, 0x60
0098E7DC  49 8D 43 B8                     lea rax, [r11 - 0x48]
0098E7E0  49 89 4B B8                     mov qword ptr [r11 - 0x48], rcx
0098E7E4  48 8B 0D 45 92 4D 00            mov rcx, qword ptr [rip + 0x4d9245]
0098E7EB  33 DB                           xor ebx, ebx
0098E7ED  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
0098E7F1  48 83 C1 38                     add rcx, 0x38
0098E7F5  48 8D 04 55 02 00 00 00         lea rax, [rdx*2 + 2]
0098E7FD  49 89 5B F0                     mov qword ptr [r11 - 0x10], rbx
0098E801  49 8D 53 D8                     lea rdx, [r11 - 0x28]
0098E805  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
0098E809  49 8B F8                        mov rdi, r8
0098E80C  49 C7 43 D8 20 00 00 00         mov qword ptr [r11 - 0x28], 0x20
0098E814  49 C7 43 E8 01 00 00 00         mov qword ptr [r11 - 0x18], 1
0098E81C  49 89 5B C0                     mov qword ptr [r11 - 0x40], rbx
0098E820  49 C7 43 D0 02 00 00 00         mov qword ptr [r11 - 0x30], 2
0098E828  E8 87 06 00 00                  call 0x14098eeb4
0098E82D  48 85 C0                        test rax, rax
0098E830  74 11                           je 0x14098e843
0098E832  48 89 07                        mov qword ptr [rdi], rax
0098E835  8B C3                           mov eax, ebx
0098E837  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0098E83C  48 83 C4 60                     add rsp, 0x60
0098E840  5F                              pop rdi
0098E841  C3                              ret
0098E842  CC                              int3
0098E843  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0098E848  EB EB                           jmp 0x14098e835
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEtStringIntern(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (96);
    *(unsigned __int64 *)(v_rsp - 72) = a1;
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp - 72;
    a1 = (*(unsigned __int64 *)(v_rip + 5083717)) + (56);
    *(unsigned __int64 *)(v_rsp - 16) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = a2 * 2 + 2;
    *(unsigned __int64 *)(v_rsp - 40) = 32;
    *(unsigned __int64 *)(v_rsp - 24) = 1;
    *(unsigned __int64 *)(v_rsp - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 48) = 2;
    result = RtlInternTableIntern(a1, v_rsp - 40, a3, a4);
    if (result == 0) goto loc_0098E843;
    *(unsigned __int64 *)(a3) = result;
loc_0098E835:
    v_rsp = (v_rsp) + (96);
    return 0;
loc_0098E843:
    goto loc_0098E835;
}
```

## 5. (Beta) C Style

```c
int64_t PopEtStringIntern(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (96);
    *(uint64_t *)(local_rsp - 0x48) = Arg1;
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x20) = local_rsp - 72;
    Arg1 = (*(uint64_t *)(v_rip + 0x4D9245)) + (56);
    *(uint64_t *)(local_rsp - 0x10) = 0;
    *(uint64_t *)(local_rsp - 0x38) = Arg2 * 2 + 2;
    *(uint64_t *)(local_rsp - 0x28) = 32;
    *(uint64_t *)(local_rsp - 0x18) = 1;
    *(uint64_t *)(local_rsp - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x30) = 2;
    result = RtlInternTableIntern(Arg1, local_rsp - 40, Arg3, a4);
    if (result == 0) goto loc_0098E843;
    *(uint64_t *)(arg3) = result;
loc_0098E835:
    local_rsp = (local_rsp) + (96);
    return 0;
loc_0098E843:
    goto loc_0098E835;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098E7D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0098E7D0[BB_0098E7D0]
  bb_0098E832[BB_0098E832]
  bb_0098E835[BB_0098E835]
  bb_0098E842[BB_0098E842]
  bb_0098E843[BB_0098E843]
  bb_0098E7D0 -->|branch| bb_0098E843
  bb_0098E7D0 -->|fallthrough| bb_0098E832
  bb_0098E832 -->|flow| bb_0098E835
  bb_0098E842 -->|flow| bb_0098E843
  bb_0098E843 -->|branch| bb_0098E835
```
