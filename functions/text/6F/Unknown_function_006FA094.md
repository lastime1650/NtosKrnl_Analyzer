# sub_006FA094

- RVA: `0x006FA094`–`0x006FA0AD` (길이 `25` bytes)
- VA: `0x00000001406FA094`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B7CC4`
- 디코드: `6`개 명령, `25/25` bytes 표시
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
- `0x006FA09E` → RVA `0x00F0DEE8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006FA0A8` → [PopUpdateWakeSource + 0x56](../4A/PopUpdateWakeSource_function_004AA70C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006FA094  48 89 0B                        mov qword ptr [rbx], rcx
006FA097  48 89 43 08                     mov qword ptr [rbx + 8], rax
006FA09B  48 89 18                        mov qword ptr [rax], rbx
006FA09E  48 89 1D 43 3E 81 00            mov qword ptr [rip + 0x813e43], rbx
006FA0A5  48 8B DF                        mov rbx, rdi
006FA0A8  E9 B5 06 DB FF                  jmp 0x1404aa762
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006FA094(__int64 a1)
{
    *(unsigned __int64 *)(v_rbx) = a1;
    *(unsigned __int64 *)(v_rbx + 8) = result;
    *(unsigned __int64 *)(result) = v_rbx;
    *(unsigned __int64 *)(v_rip + 8470083) = v_rbx;
}
```

## 5. (Beta) C Style

```c
void sub_006FA094(int64_t Arg1)
{
    *(uint64_t *)(local_rbx) = Arg1;
    *(uint64_t *)(local_rbx + 0x8) = result;
    *(uint64_t *)(result) = local_rbx;
    *(uint64_t *)(v_rip + 0x813E43) = local_rbx;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006FA094&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FA094[BB_006FA094]
```
