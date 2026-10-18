# sub_0099DDC2

- RVA: `0x0099DDC2`–`0x0099DDDA` (길이 `24` bytes)
- VA: `0x000000014099DDC2`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A17C`
- 디코드: `6`개 명령, `24/24` bytes 표시
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
  - `0x0099DDC9` → [sub_0099DD1B + 0x17](Unknown_function_0099DD1B.md) (`tail-transfer`)
  - `0x0099DDD5` → [sub_0099DD1B + 0x24](Unknown_function_0099DD1B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0099DDC2  48 8B 4A 38                     mov rcx, qword ptr [rdx + 0x38]
0099DDC6  48 85 C9                        test rcx, rcx
0099DDC9  0F 84 63 FF FF FF               je 0x14099dd32
0099DDCF  48 3B C1                        cmp rax, rcx
0099DDD2  0F 94 C0                        sete al
0099DDD5  E9 65 FF FF FF                  jmp 0x14099dd3f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0099DDC2(__int64 a1, __int64 a2)
{
    __int64 result;

    result = (result == (*(unsigned __int64 *)(a2 + 56))) ? 1 : 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0099DDC2(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    result = (result == (*(uint64_t *)(arg2 + 0x38))) ? 1 : 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099DDC2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0099DDC2[BB_0099DDC2]
  bb_0099DDCF[BB_0099DDCF]
  bb_0099DDC2 -->|fallthrough| bb_0099DDCF
```
