# sub_002F7FAE

- RVA: `0x002F7FAE`–`0x002F7FCA` (길이 `28` bytes)
- VA: `0x00000001402F7FAE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000724F4`
- 디코드: `7`개 명령, `28/28` bytes 표시
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
  - `0x002F7FB1` → [sub_002F7D3D](Unknown_function_002F7D3D.md) (`tail-transfer`)
  - `0x002F7FC5` → [sub_002F7DE0](Unknown_function_002F7DE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F7FAE  48 3B D9                        cmp rbx, rcx
002F7FB1  0F 83 86 FD FF FF               jae 0x1402f7d3d
002F7FB7  C7 06 0A 00 00 00               mov dword ptr [rsi], 0xa
002F7FBD  B0 01                           mov al, 1
002F7FBF  48 89 0F                        mov qword ptr [rdi], rcx
002F7FC2  49 89 16                        mov qword ptr [r14], rdx
002F7FC5  E9 16 FE FF FF                  jmp 0x1402f7de0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002F7FAE(__int64 a1, __int64 a2)
{
    *(unsigned int *)(v_rsi) = 10;
    *(unsigned __int64 *)(v_rdi) = a1;
    *(unsigned __int64 *)(v_r14) = a2;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002F7FAE(int64_t Arg1, int64_t Arg2)
{
    *(uint32_t *)(local_rsi) = 10;
    *(uint64_t *)(local_rdi) = Arg1;
    *(uint64_t *)(local_r14) = Arg2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F7FAE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F7FAE[BB_002F7FAE]
  bb_002F7FB7[BB_002F7FB7]
  bb_002F7FAE -->|fallthrough| bb_002F7FB7
```
