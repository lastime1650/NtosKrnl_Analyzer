# sub_00B1BBBE

- RVA: `0x00B1BBBE`–`0x00B1BBD5` (길이 `23` bytes)
- VA: `0x0000000140B1BBBE`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008533C`
- 디코드: `6`개 명령, `23/23` bytes 표시
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
  - `0x00B1BBD0` → [PspMapSystemDll + 0x13E](../8D/PspMapSystemDll_function_008D6908.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1BBBE  48 8B 50 30                     mov rdx, qword ptr [rax + 0x30]
00B1BBC2  48 89 53 20                     mov qword ptr [rbx + 0x20], rdx
00B1BBC6  8B 40 50                        mov eax, dword ptr [rax + 0x50]
00B1BBC9  89 43 0C                        mov dword ptr [rbx + 0xc], eax
00B1BBCC  4C 89 73 28                     mov qword ptr [rbx + 0x28], r14
00B1BBD0  E9 71 AE DB FF                  jmp 0x1408d6a46
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B1BBBE(void)
{
    *(unsigned __int64 *)(v_rbx + 32) = *(unsigned __int64 *)(result + 48);
    *(unsigned int *)(v_rbx + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 80)));
    *(unsigned __int64 *)(v_rbx + 40) = v_r14;
}
```

## 5. (Beta) C Style

```c
void sub_00B1BBBE(void)
{
    *(uint64_t *)(local_rbx + 0x20) = *(uint64_t *)(result + 0x30);
    *(uint32_t *)(local_rbx + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x50)));
    *(uint64_t *)(local_rbx + 0x28) = local_r14;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1BBBE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1BBBE[BB_00B1BBBE]
```
