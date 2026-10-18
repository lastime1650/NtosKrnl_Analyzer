# HalpInterruptPowerComponentIdleCallback

- RVA: `0x00558750`–`0x00558780` (길이 `48` bytes)
- VA: `0x0000000140558750`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `15`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00558761` → [HalpInterruptPowerChange](HalpInterruptPowerChange_function_00558690.md) (function, `0x00558690`)
- `0x0055876F` → [PoFxCompleteIdleCondition](../46/PoFxCompleteIdleCondition_function_00461CC0.md) (function, `0x00461CC0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00558750  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00558755  57                              push rdi
00558756  48 83 EC 20                     sub rsp, 0x20
0055875A  8B DA                           mov ebx, edx
0055875C  48 8B F9                        mov rdi, rcx
0055875F  33 D2                           xor edx, edx
00558761  E8 2A FF FF FF                  call 0x140558690
00558766  48 8B 8F 70 01 00 00            mov rcx, qword ptr [rdi + 0x170]
0055876D  8B D3                           mov edx, ebx
0055876F  E8 4C 95 F0 FF                  call 0x140461cc0
00558774  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00558779  48 83 C4 20                     add rsp, 0x20
0055877D  5F                              pop rdi
0055877E  C3                              ret
0055877F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInterruptPowerComponentIdleCallback(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = HalpInterruptPowerChange(a1, a2, a3, a4);
    result = PoFxCompleteIdleCondition(*(unsigned __int64 *)(a1 + 368), (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpInterruptPowerComponentIdleCallback(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = HalpInterruptPowerChange(Arg1, Arg2, a3, a4);
    result = PoFxCompleteIdleCondition(*(uint64_t *)(arg1 + 0x170), (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x170` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00558750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00558750[BB_00558750]
  bb_0055877F[BB_0055877F]
```
