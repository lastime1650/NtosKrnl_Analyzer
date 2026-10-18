# sub_00BBC33A

- RVA: `0x00BBC33A`–`0x00BBC34E` (길이 `20` bytes)
- VA: `0x0000000140BBC33A`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B514C`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BBC340` → [ViRemLockDeleteFirstTreeNode](../BA/ViRemLockDeleteFirstTreeNode_function_00BA28F4.md) (function, `0x00BA28F4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00BBC349` → [VfRemLockDeleteMemoryRange + 0x3A](VfRemLockDeleteMemoryRange_function_00BB7AEC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00BBC33A  48 8B D7                        mov rdx, rdi
00BBC33D  48 8B CE                        mov rcx, rsi
00BBC340  E8 AF 65 FE FF                  call 0x140ba28f4
00BBC345  85 C0                           test eax, eax
00BBC347  75 F1                           jne 0x140bbc33a
00BBC349  E9 D8 B7 FF FF                  jmp 0x140bb7b26
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00BBC33A(void)
{
    __int64 result;

    result = ViRemLockDeleteFirstTreeNode(v_rsi, v_rdi, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00BBC33A;
}
```

## 5. (Beta) C Style

```c
void sub_00BBC33A(void)
{
    int64_t result;

    result = ViRemLockDeleteFirstTreeNode(local_rsi, local_rdi, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_00BBC33A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BBC33A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BBC33A[BB_00BBC33A]
  bb_00BBC349[BB_00BBC349]
  bb_00BBC33A -->|branch| bb_00BBC33A
  bb_00BBC33A -->|fallthrough| bb_00BBC349
```
