# ExpQueueWorkItem

- RVA: `0x00358400`–`0x00358409` (길이 `9` bytes)
- VA: `0x0000000140358400`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079714`
- 디코드: `4`개 명령, `9/9` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_002F955F](../2F/Unknown_function_002F955F.md) at `0x002F9591`
- [ExQueueWorkItemEx](ExQueueWorkItemEx_function_003567B0.md) at `0x003567EC`
- [ExQueueWorkItemToPartition](ExQueueWorkItemToPartition_function_00356E2C.md) at `0x00356E6C`
- [sub_0035832F](Unknown_function_0035832F.md) at `0x00358363`
- [ExQueueWorkItemExFromIo](../43/ExQueueWorkItemExFromIo_function_0043CB58.md) at `0x0043CB97`
- [ExQueueWorkItemToPrivatePool](../47/ExQueueWorkItemToPrivatePool_function_0047D3B4.md) at `0x0047D3FD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00358400  48 8B C4                        mov rax, rsp
00358403  53                              push rbx
00358404  57                              push rdi
00358405  48 83 EC 78                     sub rsp, 0x78
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpQueueWorkItem(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (120);
    return v_rsp;
}
```

## 5. (Beta) C Style

```c
void ExpQueueWorkItem(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (120);
    return local_rsp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00358400&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00358400[BB_00358400]
```
