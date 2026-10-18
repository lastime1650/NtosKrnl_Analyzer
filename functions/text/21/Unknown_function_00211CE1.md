# sub_00211CE1

- RVA: `0x00211CE1`–`0x00211CF4` (길이 `19` bytes)
- VA: `0x0000000140211CE1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DEB4`
- 디코드: `6`개 명령, `19/19` bytes 표시
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
  - `0x00211CE3` → [sub_00211C19 + 0x32](Unknown_function_00211C19.md) (`tail-transfer`)
  - `0x00211CF2` → [sub_00211C19 + 0x8B](Unknown_function_00211C19.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00211CE1  A8 04                           test al, 4
00211CE3  0F 85 62 FF FF FF               jne 0x140211c4b
00211CE9  8D 41 01                        lea eax, [rcx + 1]
00211CEC  40 B7 01                        mov dil, 1
00211CEF  89 46 20                        mov dword ptr [rsi + 0x20], eax
00211CF2  EB B0                           jmp 0x140211ca4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00211CE1(__int64 a1)
{
    *(unsigned int *)(v_rsi + 32) = (unsigned int)(a1 + 1);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00211CE1(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint32_t *)(local_rsi + 0x20) = (uint32_t)(Arg1 + 1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00211CE1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00211CE1[BB_00211CE1]
  bb_00211CE9[BB_00211CE9]
  bb_00211CE1 -->|fallthrough| bb_00211CE9
```
