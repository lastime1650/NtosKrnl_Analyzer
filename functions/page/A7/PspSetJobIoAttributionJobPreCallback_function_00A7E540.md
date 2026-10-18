# PspSetJobIoAttributionJobPreCallback

- RVA: `0x00A7E540`–`0x00A7E564` (길이 `36` bytes)
- VA: `0x0000000140A7E540`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A7E540  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
00A7E544  4C 8B C1                        mov r8, rcx
00A7E547  49 3B C9                        cmp rcx, r9
00A7E54A  75 04                           jne 0x140a7e550
00A7E54C  33 C0                           xor eax, eax
00A7E54E  C3                              ret
00A7E54F  CC                              int3
00A7E550  8A 42 10                        mov al, byte ptr [rdx + 0x10]
00A7E553  F6 D8                           neg al
00A7E555  48 1B C9                        sbb rcx, rcx
00A7E558  49 23 C9                        and rcx, r9
00A7E55B  49 89 88 30 06 00 00            mov qword ptr [r8 + 0x630], rcx
00A7E562  EB E8                           jmp 0x140a7e54c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspSetJobIoAttributionJobPreCallback(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a1 != (*(unsigned __int64 *)(a2 + 8))) goto loc_00A7E550;
loc_00A7E54C:
    result = 0;
    return result;
loc_00A7E550:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a2 + 16)));
    a1 = (a1) & (*(unsigned __int64 *)(a2 + 8));
    *(unsigned __int64 *)(a1 + 1584) = a1;
    goto loc_00A7E54C;
}
```

## 5. (Beta) C Style

```c
int64_t PspSetJobIoAttributionJobPreCallback(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (Arg1 != (*(uint64_t *)(arg2 + 0x8))) goto loc_00A7E550;
loc_00A7E54C:
    result = 0;
    return result;
loc_00A7E550:
    result = (uint8_t)(-(*(uint8_t *)(arg2 + 0x10)));
    Arg1 = (Arg1) & (*(uint64_t *)(arg2 + 0x8));
    *(void **)(arg1 + 0x630) = Arg1;
    goto loc_00A7E54C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x630` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A7E540&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A7E540[BB_00A7E540]
  bb_00A7E54C[BB_00A7E54C]
  bb_00A7E54F[BB_00A7E54F]
  bb_00A7E550[BB_00A7E550]
  bb_00A7E540 -->|branch| bb_00A7E550
  bb_00A7E540 -->|fallthrough| bb_00A7E54C
  bb_00A7E54F -->|flow| bb_00A7E550
  bb_00A7E550 -->|branch| bb_00A7E54C
```
