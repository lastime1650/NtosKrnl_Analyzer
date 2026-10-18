# sub_0085CAD4

- RVA: `0x0085CAD4`–`0x0085CAEF` (길이 `27` bytes)
- VA: `0x000000014085CAD4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006AF48`
- 디코드: `6`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085CAE5` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0085CAD9` → [sub_0085CA0D + 0x7B](Unknown_function_0085CA0D.md) (`tail-transfer`)
  - `0x0085CAE0` → [sub_0085C997 + 0x34](Unknown_function_0085C997.md) (`tail-transfer`)
  - `0x0085CAEA` → [sub_0085C997 + 0x34](Unknown_function_0085C997.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085CAD4  44 8B 74 81 04                  mov r14d, dword ptr [rcx + rax*4 + 4]
0085CAD9  EB AD                           jmp 0x14085ca88
0085CADB  44 8B 74 83 04                  mov r14d, dword ptr [rbx + rax*4 + 4]
0085CAE0  E9 E6 FE FF FF                  jmp 0x14085c9cb
0085CAE5  E8 36 01 00 00                  call 0x14085cc20
0085CAEA  E9 DC FE FF FF                  jmp 0x14085c9cb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0085CAD4(__int64 a1)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_0085CAD4(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4 + rax*4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085CAD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085CAD4[BB_0085CAD4]
  bb_0085CADB[BB_0085CADB]
  bb_0085CAE5[BB_0085CAE5]
```
