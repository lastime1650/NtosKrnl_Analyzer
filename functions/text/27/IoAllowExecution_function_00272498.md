# IoAllowExecution

- RVA: `0x00272498`–`0x002724D0` (길이 `56` bytes)
- VA: `0x0000000140272498`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BAC`
- 디코드: `20`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002724A2` → [IopGetDevicePDO](IopGetDevicePDO_function_002724D8.md) (function, `0x002724D8`)
- `0x002724B7` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [sub_00984B34](../../page/98/Unknown_function_00984B34.md) at `0x00984C45`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00272498  40 53                           push rbx
0027249A  48 83 EC 20                     sub rsp, 0x20
0027249E  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
002724A2  E8 31 00 00 00                  call 0x1402724d8
002724A7  48 85 C0                        test rax, rax
002724AA  74 20                           je 0x1402724cc
002724AC  8B 58 30                        mov ebx, dword ptr [rax + 0x30]
002724AF  BA 44 66 6C 74                  mov edx, 0x746c6644
002724B4  48 8B C8                        mov rcx, rax
002724B7  E8 24 54 08 00                  call 0x1402f78e0
002724BC  C1 EB 17                        shr ebx, 0x17
002724BF  B0 01                           mov al, 1
002724C1  F6 D3                           not bl
002724C3  22 C3                           and al, bl
002724C5  48 83 C4 20                     add rsp, 0x20
002724C9  5B                              pop rbx
002724CA  C3                              ret
002724CB  CC                              int3
002724CC  B0 01                           mov al, 1
002724CE  EB F5                           jmp 0x1402724c5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoAllowExecution(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = IopGetDevicePDO(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    if (result == 0) goto loc_002724CC;
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x746C6644ULL), a3, a4);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) >> (23));
    v_rbx = (unsigned __int8)(~(v_rbx));
    result = (unsigned __int8)((1) & ((unsigned __int8)(v_rbx)));
loc_002724C5:
    v_rsp = (v_rsp) + (32);
    return result;
loc_002724CC:
    goto loc_002724C5;
}
```

## 5. (Beta) C Style

```c
int64_t IoAllowExecution(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = IopGetDevicePDO(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    if (result == 0) goto loc_002724CC;
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x746C6644ULL), a3, a4);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) >> (23));
    local_rbx = (uint8_t)(~(local_rbx));
    result = (uint8_t)((1) & ((uint8_t)(local_rbx)));
loc_002724C5:
    local_rsp = (local_rsp) + (32);
    return result;
loc_002724CC:
    goto loc_002724C5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00272498&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00272498[BB_00272498]
  bb_002724AC[BB_002724AC]
  bb_002724C5[BB_002724C5]
  bb_002724CB[BB_002724CB]
  bb_002724CC[BB_002724CC]
  bb_00272498 -->|branch| bb_002724CC
  bb_00272498 -->|fallthrough| bb_002724AC
  bb_002724AC -->|flow| bb_002724C5
  bb_002724CB -->|flow| bb_002724CC
  bb_002724CC -->|branch| bb_002724C5
```
