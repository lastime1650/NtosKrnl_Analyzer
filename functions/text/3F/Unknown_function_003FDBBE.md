# sub_003FDBBE

- RVA: `0x003FDBBE`–`0x003FDBD9` (길이 `27` bytes)
- VA: `0x00000001403FDBBE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00099CCC`
- 디코드: `6`개 명령, `27/27` bytes 표시
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
- `0x003FDBC3` → RVA `0x00F8F998` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003FDBD3` → [sub_003FDD70](Unknown_function_003FDD70.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FDBBE  4C 89 64 24 10                  mov qword ptr [rsp + 0x10], r12
003FDBC3  44 8B 25 CE 1D B9 00            mov r12d, dword ptr [rip + 0xb91dce]
003FDBCA  43 8D 04 64                     lea eax, [r12 + r12*2]
003FDBCE  C1 E0 03                        shl eax, 3
003FDBD1  3B C8                           cmp ecx, eax
003FDBD3  0F 82 97 01 00 00               jb 0x1403fdd70
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003FDBBE(int a1)
{
    __int64 result;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_r12;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12131790)) + (unsigned int)(*(unsigned int *)(v_rip + 12131790)) * 2) << (3));
}
```

## 5. (Beta) C Style

```c
int64_t sub_003FDBBE(int32_t Arg1)
{
    int64_t result;
    uint64_t v_stack_p10;

    v_stack_p10 = local_r12;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB91DCE)) + (uint32_t)(*(uint32_t *)(v_rip + 0xB91DCE)) * 2) << (3));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FDBBE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FDBBE[BB_003FDBBE]
```
