# sub_006F481E

- RVA: `0x006F481E`–`0x006F483B` (길이 `29` bytes)
- VA: `0x00000001406F481E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ACEB0`
- 디코드: `9`개 명령, `29/29` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F4836` → [RtlpHpSegSegmentInitialize + 0x7C](../47/RtlpHpSegSegmentInitialize_function_00478EB0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F481E  45 3B C1                        cmp r8d, r9d
006F4821  41 8B C1                        mov eax, r9d
006F4824  41 0F 42 C0                     cmovb eax, r8d
006F4828  0F B6 C0                        movzx eax, al
006F482B  88 01                           mov byte ptr [rcx], al
006F482D  48 8D 49 20                     lea rcx, [rcx + 0x20]
006F4831  44 2B C0                        sub r8d, eax
006F4834  75 E8                           jne 0x1406f481e
006F4836  E9 F1 46 D8 FF                  jmp 0x140478f2c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F481E(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;

    result = (unsigned int)(a4);
    if (a3 < a4) { result = a3; }
    *(unsigned __int8 *)(a1) = (unsigned __int8)((unsigned __int8)(result));
    a3 = (unsigned int)((a3) - ((unsigned int)((unsigned __int8)(result))));
    if (condition_is_not_equal) goto loc_006F481E;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F481E(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint32_t)(Arg4);
    if (Arg3 < Arg4) { result = Arg3; }
    *(uint8_t *)(arg1) = (uint8_t)((uint8_t)(result));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)((uint8_t)(result))));
    if (condition_is_not_equal) goto loc_006F481E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F481E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F481E[BB_006F481E]
  bb_006F4836[BB_006F4836]
  bb_006F481E -->|branch| bb_006F481E
  bb_006F481E -->|fallthrough| bb_006F4836
```
