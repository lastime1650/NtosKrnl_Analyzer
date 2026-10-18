# sub_006F7986

- RVA: `0x006F7986`–`0x006F79AC` (길이 `38` bytes)
- VA: `0x00000001406F7986`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B47A4`
- 디코드: `9`개 명령, `38/38` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006F799B` → [RtlpHpVaMgrRangeCommitProcess + 0x117](../49/RtlpHpVaMgrRangeCommitProcess_function_0049A444.md) (`tail-transfer`)
  - `0x006F79A7` → [RtlpHpVaMgrRangeCommitProcess + 0x117](../49/RtlpHpVaMgrRangeCommitProcess_function_0049A444.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F7986  0F B7 C8                        movzx ecx, ax
006F7989  66 41 23 CA                     and cx, r10w
006F798D  66 F0 41 0F B1 08               lock cmpxchg word ptr [r8], cx
006F7993  75 F1                           jne 0x1406f7986
006F7995  66 23 C2                        and ax, dx
006F7998  66 3B E8                        cmp bp, ax
006F799B  0F 84 BA 2B DA FF               je 0x14049a55b
006F79A1  41 BB 02 00 00 00               mov r11d, 2
006F79A7  E9 AF 2B DA FF                  jmp 0x14049a55b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F7986(__int64 a1, unsigned __int16 a2, __int64 a3)
{
    __int64 result;

    a1 = (unsigned __int16)(((unsigned __int16)(result)) & ((unsigned __int16)(v_r10)));
    if (condition_is_not_equal) goto loc_006F7986;
    result = (unsigned __int16)((result) & (a2));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F7986(int64_t Arg1, uint16_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    Arg1 = (uint16_t)(((uint16_t)(result)) & ((uint16_t)(local_r10)));
    if (condition_is_not_equal) goto loc_006F7986;
    result = (uint16_t)((result) & (Arg2));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F7986&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F7986[BB_006F7986]
  bb_006F7995[BB_006F7995]
  bb_006F79A1[BB_006F79A1]
  bb_006F7986 -->|branch| bb_006F7986
  bb_006F7986 -->|fallthrough| bb_006F7995
  bb_006F7995 -->|fallthrough| bb_006F79A1
```
