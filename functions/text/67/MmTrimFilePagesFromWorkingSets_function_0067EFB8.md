# MmTrimFilePagesFromWorkingSets

- RVA: `0x0067EFB8`–`0x0067EFEF` (길이 `55` bytes)
- VA: `0x000000014067EFB8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `18`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0067EFD3` → [MiQueueWorkingSetRequest](../4F/MiQueueWorkingSetRequest_function_004F7168.md) (function, `0x004F7168`)
- `0x0067EFDB` → [PsGetNextPartition](../3B/PsGetNextPartition_function_003B9D5C.md) (function, `0x003B9D5C`)

### Direct callers
- [sub_00B8053E](../../pagelk/B8/Unknown_function_00B8053E.md) at `0x00B805C0`

### Static image references
- `0x0067EFBE` → RVA `0x00E37614` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0067EFB8  40 53                           push rbx
0067EFBA  48 83 EC 20                     sub rsp, 0x20
0067EFBE  80 3D 4F 86 7B 00 00            cmp byte ptr [rip + 0x7b864f], 0
0067EFC5  74 21                           je 0x14067efe8
0067EFC7  33 C9                           xor ecx, ecx
0067EFC9  EB 10                           jmp 0x14067efdb
0067EFCB  48 8B 0B                        mov rcx, qword ptr [rbx]
0067EFCE  BA 80 00 00 00                  mov edx, 0x80
0067EFD3  E8 90 81 E7 FF                  call 0x1404f7168
0067EFD8  48 8B CB                        mov rcx, rbx
0067EFDB  E8 7C AD D3 FF                  call 0x1403b9d5c
0067EFE0  48 8B D8                        mov rbx, rax
0067EFE3  48 85 C0                        test rax, rax
0067EFE6  75 E3                           jne 0x14067efcb
0067EFE8  48 83 C4 20                     add rsp, 0x20
0067EFEC  5B                              pop rbx
0067EFED  C3                              ret
0067EFEE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmTrimFilePagesFromWorkingSets(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int8 *)(v_rip + 8095311)) == 0) goto loc_0067EFE8;
    a1 = 0;
    goto loc_0067EFDB;
loc_0067EFCB:
    result = MiQueueWorkingSetRequest(*(unsigned __int64 *)(v_rbx), 128, a3, a4);
loc_0067EFDB:
    result = PsGetNextPartition(v_rbx, 128, a3, a4);
    if (result != 0) goto loc_0067EFCB;
loc_0067EFE8:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmTrimFilePagesFromWorkingSets(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint8_t *)(v_rip + 0x7B864F)) == 0) goto loc_0067EFE8;
    Arg1 = 0;
    goto loc_0067EFDB;
loc_0067EFCB:
    result = MiQueueWorkingSetRequest(*(uint64_t *)(local_rbx), 128, a3, a4);
loc_0067EFDB:
    result = PsGetNextPartition(local_rbx, 128, a3, a4);
    if (result != 0) goto loc_0067EFCB;
loc_0067EFE8:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0067EFB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0067EFB8[BB_0067EFB8]
  bb_0067EFC7[BB_0067EFC7]
  bb_0067EFCB[BB_0067EFCB]
  bb_0067EFDB[BB_0067EFDB]
  bb_0067EFE8[BB_0067EFE8]
  bb_0067EFEE[BB_0067EFEE]
  bb_0067EFB8 -->|branch| bb_0067EFE8
  bb_0067EFB8 -->|fallthrough| bb_0067EFC7
  bb_0067EFC7 -->|branch| bb_0067EFDB
  bb_0067EFCB -->|flow| bb_0067EFDB
  bb_0067EFDB -->|branch| bb_0067EFCB
  bb_0067EFDB -->|fallthrough| bb_0067EFE8
```
