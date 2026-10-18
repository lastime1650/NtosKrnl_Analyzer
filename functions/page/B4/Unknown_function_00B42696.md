# sub_00B42696

- RVA: `0x00B42696`–`0x00B426A8` (길이 `18` bytes)
- VA: `0x0000000140B42696`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B664C`
- 디코드: `5`개 명령, `18/18` bytes 표시
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
  - `0x00B426A3` → [ExpCreateOutputNT + 0x39](../A7/ExpCreateOutputNT_function_00A7B53C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B42696  48 FF C0                        inc rax
00B42699  66 45 39 24 41                  cmp word ptr [r9 + rax*2], r12w
00B4269E  75 F6                           jne 0x140b42696
00B426A0  8D 3C 47                        lea edi, [rdi + rax*2]
00B426A3  E9 CD 8E F3 FF                  jmp 0x140a7b575
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B42696(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;

    result = (result) + 1;
    if ((*(unsigned __int16 *)(a4 + result * 2)) != ((unsigned __int16)(v_r12))) goto loc_00B42696;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B42696(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;

    result = (result) + 1;
    if ((*(uint16_t *)(arg4 + result * 2)) != ((uint16_t)(local_r12))) goto loc_00B42696;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0 + rax*2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B42696&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B42696[BB_00B42696]
  bb_00B426A0[BB_00B426A0]
  bb_00B42696 -->|branch| bb_00B42696
  bb_00B42696 -->|fallthrough| bb_00B426A0
```
