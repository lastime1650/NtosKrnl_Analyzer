# sub_008E0776

- RVA: `0x008E0776`–`0x008E078C` (길이 `22` bytes)
- VA: `0x00000001408E0776`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085D68`
- 디코드: `8`개 명령, `22/22` bytes 표시
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
  - `0x008E077D` → [sub_008E06CC + 0x4B](Unknown_function_008E06CC.md) (`tail-transfer`)
  - `0x008E078A` → [sub_008E06CC + 0x4B](Unknown_function_008E06CC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008E0776  48 8B F0                        mov rsi, rax
008E0779  48 39 58 10                     cmp qword ptr [rax + 0x10], rbx
008E077D  74 98                           je 0x1408e0717
008E077F  48 8B 00                        mov rax, qword ptr [rax]
008E0782  48 8B F7                        mov rsi, rdi
008E0785  48 3B C1                        cmp rax, rcx
008E0788  75 EC                           jne 0x1408e0776
008E078A  EB 8B                           jmp 0x1408e0717
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008E0776(__int64 a1)
{
    if ((*(unsigned __int64 *)(result)) != a1) goto loc_008E0776;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008E0776(int64_t Arg1)
{
    if ((*(uint64_t *)(result)) != Arg1) goto loc_008E0776;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E0776&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E0776[BB_008E0776]
  bb_008E077F[BB_008E077F]
  bb_008E078A[BB_008E078A]
  bb_008E0776 -->|fallthrough| bb_008E077F
  bb_008E077F -->|branch| bb_008E0776
  bb_008E077F -->|fallthrough| bb_008E078A
```
