# sub_006E76DC

- RVA: `0x006E76DC`–`0x006E76F4` (길이 `24` bytes)
- VA: `0x00000001406E76DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C834`
- 디코드: `5`개 명령, `24/24` bytes 표시
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
- `0x006E76DC` → RVA `0x00E2DBD0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E76EF` → [MiFindPagesForMdl + 0x45](../3B/MiFindPagesForMdl_function_003B770C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E76DC  48 8B 05 ED 64 74 00            mov rax, qword ptr [rip + 0x7464ed]
006E76E3  41 0F AF C8                     imul ecx, r8d
006E76E7  48 8D 34 88                     lea rsi, [rax + rcx*4]
006E76EB  4A 8D 04 86                     lea rax, [rsi + r8*4]
006E76EF  E9 5D 00 CD FF                  jmp 0x1403b7751
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E76DC(int a1, __int64 a2, __int64 a3)
{
    a1 = (unsigned int)((a1) * ((unsigned int)(a3)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E76DC(int32_t Arg1, int64_t Arg2, int64_t Arg3)
{
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(Arg3)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E76DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E76DC[BB_006E76DC]
```
