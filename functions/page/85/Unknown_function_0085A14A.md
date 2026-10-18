# sub_0085A14A

- RVA: `0x0085A14A`–`0x0085A164` (길이 `26` bytes)
- VA: `0x000000014085A14A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006AB14`
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
  - `0x0085A153` → [sub_0085A217](Unknown_function_0085A217.md) (`tail-transfer`)
  - `0x0085A15F` → [sub_00859FB9 + 0x4D](Unknown_function_00859FB9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085A14A  C1 EB 04                        shr ebx, 4
0085A14D  81 FB FF 00 00 00               cmp ebx, 0xff
0085A153  0F 87 BE 00 00 00               ja 0x14085a217
0085A159  0F BD DB                        bsr ebx, ebx
0085A15C  83 C3 10                        add ebx, 0x10
0085A15F  E9 A2 FE FF FF                  jmp 0x14085a006
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0085A14A(void)
{
    __int64 v_rbx;

    v_rbx = (unsigned int)((v_rbx) >> (4));
    v_rbx = (unsigned int)((v_rbx) + (16));
}
```

## 5. (Beta) C Style

```c
void sub_0085A14A(void)
{
    int64_t local_rbx;

    local_rbx = (uint32_t)((local_rbx) >> (4));
    local_rbx = (uint32_t)((local_rbx) + (16));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085A14A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085A14A[BB_0085A14A]
  bb_0085A159[BB_0085A159]
  bb_0085A14A -->|fallthrough| bb_0085A159
```
