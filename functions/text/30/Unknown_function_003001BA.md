# sub_003001BA

- RVA: `0x003001BA`–`0x003001D4` (길이 `26` bytes)
- VA: `0x00000001403001BA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00072FCC`
- 디코드: `7`개 명령, `26/26` bytes 표시
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
  - `0x003001C8` → [sub_00300164 + 0x1C](Unknown_function_00300164.md) (`tail-transfer`)
  - `0x003001CF` → [sub_0030012B + 0x5](Unknown_function_0030012B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003001BA  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
003001BE  48 8B 10                        mov rdx, qword ptr [rax]
003001C1  48 8D 41 48                     lea rax, [rcx + 0x48]
003001C5  48 3B D0                        cmp rdx, rax
003001C8  75 B6                           jne 0x140300180
003001CA  B8 1A 00 00 80                  mov eax, 0x8000001a
003001CF  E9 5C FF FF FF                  jmp 0x140300130
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003001BA(__int64 a1)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_003001BA(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003001BA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003001BA[BB_003001BA]
  bb_003001CA[BB_003001CA]
  bb_003001BA -->|fallthrough| bb_003001CA
```
