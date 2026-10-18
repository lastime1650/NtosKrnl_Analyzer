# _pctype_func

- RVA: `0x00503CFC`–`0x00503D05` (길이 `9` bytes)
- VA: `0x0000000140503CFC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `9/9` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [strtoxlX](../4F/strtoxlX_function_004FF130.md) at `0x004FF18D`
- [strtoxlX](../4F/strtoxlX_function_004FF130.md) at `0x004FF22B`
- [strtoxlX](../4F/strtoxlX_function_004FF130.md) at `0x004FF240`
- [strtoxq](../4F/strtoxq_function_004FF3F8.md) at `0x004FF443`
- [strtoxq](../4F/strtoxq_function_004FF3F8.md) at `0x004FF45C`
- [strtoxq](../4F/strtoxq_function_004FF3F8.md) at `0x004FF4E7`
- [strtoxq](../4F/strtoxq_function_004FF3F8.md) at `0x004FF4FC`
- [tolower](tolower_function_00501830.md) at `0x00501838`

### Static image references
- `0x00503CFC` → RVA `0x00E00000` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00503CFC  48 8B 05 FD C2 8F 00            mov rax, qword ptr [rip + 0x8fc2fd]
00503D03  C3                              ret
00503D04  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _pctype_func(void)
{
    return *(unsigned __int64 *)(v_rip + 9421565);
}
```

## 5. (Beta) C Style

```c
void _pctype_func(void)
{
    return *(uint64_t *)(v_rip + 0x8FC2FD);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00503CFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00503CFC[BB_00503CFC]
  bb_00503D04[BB_00503D04]
```
