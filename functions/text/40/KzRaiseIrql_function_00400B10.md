# KzRaiseIrql

- RVA: `0x00400B10`–`0x00400B41` (길이 `49` bytes)
- VA: `0x0000000140400B10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006AD84`
- 디코드: `16`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00400B3A` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [KiVirtualizationException](../6C/KiVirtualizationException_function_006C2900.md) at `0x006C2C70`

### Static image references
- `0x00400B21` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00400B10  40 53                           push rbx
00400B12  48 83 EC 20                     sub rsp, 0x20
00400B16  44 0F 20 C3                     mov rbx, cr8
00400B1A  0F B6 C1                        movzx eax, cl
00400B1D  44 0F 22 C0                     mov cr8, rax
00400B21  83 3D F8 61 BC 00 00            cmp dword ptr [rip + 0xbc61f8], 0
00400B28  75 0A                           jne 0x140400b34
00400B2A  0F B6 C3                        movzx eax, bl
00400B2D  48 83 C4 20                     add rsp, 0x20
00400B31  5B                              pop rbx
00400B32  C3                              ret
00400B33  CC                              int3
00400B34  0F B6 D1                        movzx edx, cl
00400B37  0F B6 CB                        movzx ecx, bl
00400B3A  E8 BD 4B 0F 00                  call 0x1404f56fc
00400B3F  EB E9                           jmp 0x140400b2a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KzRaiseIrql(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 12345848)) != 0) goto loc_00400B34;
loc_00400B2A:
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
loc_00400B34:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), a1, a3, a4);
    goto loc_00400B2A;
}
```

## 5. (Beta) C Style

```c
int64_t KzRaiseIrql(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xBC61F8)) != 0) goto loc_00400B34;
loc_00400B2A:
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
loc_00400B34:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), Arg1, a3, a4);
    goto loc_00400B2A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00400B10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00400B10[BB_00400B10]
  bb_00400B2A[BB_00400B2A]
  bb_00400B33[BB_00400B33]
  bb_00400B34[BB_00400B34]
  bb_00400B10 -->|branch| bb_00400B34
  bb_00400B10 -->|fallthrough| bb_00400B2A
  bb_00400B33 -->|flow| bb_00400B34
  bb_00400B34 -->|branch| bb_00400B2A
```
