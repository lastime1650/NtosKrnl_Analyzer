# NtIsSystemResumeAutomatic

- RVA: `0x00AB8DF0`–`0x00AB8DFD` (길이 `13` bytes)
- VA: `0x0000000140AB8DF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `13/13` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AB8DF0` → RVA `0x00F0CCE8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB8DF0  8B 05 F2 3E 45 00               mov eax, dword ptr [rip + 0x453ef2]
00AB8DF6  A8 03                           test al, 3
00AB8DF8  0F 94 C0                        sete al
00AB8DFB  C3                              ret
00AB8DFC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtIsSystemResumeAutomatic(void)
{
    __int64 result;

    result = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4538098)))) & (3)) == 0) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
void NtIsSystemResumeAutomatic(void)
{
    int64_t result;

    result = ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x453EF2)))) & (3)) == 0) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB8DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB8DF0[BB_00AB8DF0]
  bb_00AB8DFC[BB_00AB8DFC]
```
