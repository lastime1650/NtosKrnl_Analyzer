# RtlpHpAllocateHeap

- RVA: `0x002E98B0`–`0x002E98D9` (길이 `41` bytes)
- VA: `0x00000001402E98B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000714E8`
- 디코드: `11`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExAllocateHeapPages](../44/ExAllocateHeapPages_function_00446BB4.md) at `0x00446C08`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002E98D3` → [sub_002E9BEB + 0x1](Unknown_function_002E9BEB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E98B0  48 8B C4                        mov rax, rsp
002E98B3  56                              push rsi
002E98B4  57                              push rdi
002E98B5  41 56                           push r14
002E98B7  48 81 EC 80 00 00 00            sub rsp, 0x80
002E98BE  41 8B F8                        mov edi, r8d
002E98C1  48 8B F2                        mov rsi, rdx
002E98C4  81 E7 FA 2F 00 00               and edi, 0x2ffa
002E98CA  4C 8B F1                        mov r14, rcx
002E98CD  F7 C7 FD FF FF FF               test edi, 0xfffffffd
002E98D3  0F 85 13 03 00 00               jne 0x1402e9bec
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpAllocateHeap(__int64 a1, __int64 a2, int a3)
{
    __int64 v_rdi;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (128);
    v_rdi = (unsigned int)(((unsigned int)(a3)) & (0x2FFAULL));
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpAllocateHeap(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t local_rdi;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (128);
    local_rdi = (uint32_t)(((uint32_t)(Arg3)) & (0x2FFAULL));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E98B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E98B0[BB_002E98B0]
```
