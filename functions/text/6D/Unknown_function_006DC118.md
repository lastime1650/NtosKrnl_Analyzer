# sub_006DC118

- RVA: `0x006DC118`–`0x006DC134` (길이 `28` bytes)
- VA: `0x00000001406DC118`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E460`
- 디코드: `8`개 명령, `28/28` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DC128` → [PopQueueQuerySetIrp + 0x157](../2B/PopQueueQuerySetIrp_function_002BEF18.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DC118  48 8B C8                        mov rcx, rax
006DC11B  48 8B 40 78                     mov rax, qword ptr [rax + 0x78]
006DC11F  48 85 C0                        test rax, rax
006DC122  75 F4                           jne 0x1406dc118
006DC124  48 89 59 78                     mov qword ptr [rcx + 0x78], rbx
006DC128  E9 42 2F BE FF                  jmp 0x1402bf06f
006DC12D  B9 03 00 00 00                  mov ecx, 3
006DC132  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DC118(void)
{
    if (*(unsigned __int64 *)(result + 120) != 0) goto loc_006DC118;
    *(unsigned __int64 *)(result + 120) = v_rbx;
}
```

## 5. (Beta) C Style

```c
void sub_006DC118(void)
{
    if (*(uint64_t *)(result + 0x78) != 0) goto loc_006DC118;
    *(uint64_t *)(result + 0x78) = local_rbx;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DC118&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DC118[BB_006DC118]
  bb_006DC124[BB_006DC124]
  bb_006DC12D[BB_006DC12D]
  bb_006DC118 -->|branch| bb_006DC118
  bb_006DC118 -->|fallthrough| bb_006DC124
```
