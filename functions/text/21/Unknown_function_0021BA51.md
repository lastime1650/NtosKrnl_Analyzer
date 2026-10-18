# sub_0021BA51

- RVA: `0x0021BA51`–`0x0021BA7E` (길이 `45` bytes)
- VA: `0x000000014021BA51`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005ED90`
- 디코드: `8`개 명령, `45/45` bytes 표시
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
  - `0x0021BA5C` → [sub_0021B896 + 0x95](Unknown_function_0021B896.md) (`tail-transfer`)
  - `0x0021BA79` → [sub_0021B896 + 0x70](Unknown_function_0021B896.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0021BA51  48 F7 D1                        not rcx
0021BA54  F0 48 21 8A 90 01 00 00         lock and qword ptr [rdx + 0x190], rcx
0021BA5C  E9 CA FE FF FF                  jmp 0x14021b92b
0021BA61  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0021BA6B  8B 00                           mov eax, dword ptr [rax]
0021BA6D  2B 87 B4 01 00 00               sub eax, dword ptr [rdi + 0x1b4]
0021BA73  01 87 84 00 00 00               add dword ptr [rdi + 0x84], eax
0021BA79  E9 88 FE FF FF                  jmp 0x14021b906
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0021BA51(__int64 a1, __int64 a2)
{
    a1 = ~(a1);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0021BA51(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    Arg1 = ~(Arg1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x190` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0021BA51&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0021BA51[BB_0021BA51]
  bb_0021BA61[BB_0021BA61]
```
