# sub_008C0F95

- RVA: `0x008C0F95`–`0x008C0FAF` (길이 `26` bytes)
- VA: `0x00000001408C0F95`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083550`
- 디코드: `6`개 명령, `26/26` bytes 표시
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
  - `0x008C0F9E` → [EtwpCalculateUpdateNotification + 0x52](EtwpCalculateUpdateNotification_function_008C0BE0.md) (`tail-transfer`)
  - `0x008C0FAA` → [EtwpCalculateUpdateNotification + 0x52](EtwpCalculateUpdateNotification_function_008C0BE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C0F95  0F B7 49 68                     movzx ecx, word ptr [rcx + 0x68]
008C0F99  44 0F B7 57 64                  movzx r10d, word ptr [rdi + 0x64]
008C0F9E  E9 8F FC FF FF                  jmp 0x1408c0c32
008C0FA3  0F B7 49 6A                     movzx ecx, word ptr [rcx + 0x6a]
008C0FA7  45 8B D6                        mov r10d, r14d
008C0FAA  E9 83 FC FF FF                  jmp 0x1408c0c32
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_008C0F95(__int64 a1)
{
}
```

## 5. (Beta) C Style

```c
void sub_008C0F95(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C0F95&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C0F95[BB_008C0F95]
  bb_008C0FA3[BB_008C0FA3]
```
