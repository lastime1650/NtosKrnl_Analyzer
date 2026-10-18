# KzLowerIrql

- RVA: `0x003FCF50`–`0x003FCF79` (길이 `41` bytes)
- VA: `0x00000001403FCF50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003FCF69` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- [KiVirtualizationException](../6C/KiVirtualizationException_function_006C2900.md) at `0x006C2C9D`

### Static image references
- `0x003FCF56` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003FCF50  40 53                           push rbx
003FCF52  48 83 EC 20                     sub rsp, 0x20
003FCF56  83 3D C3 9D BC 00 00            cmp dword ptr [rip + 0xbc9dc3], 0
003FCF5D  0F B6 D9                        movzx ebx, cl
003FCF60  74 0C                           je 0x1403fcf6e
003FCF62  44 0F 20 C1                     mov rcx, cr8
003FCF66  0F B6 D3                        movzx edx, bl
003FCF69  E8 2A 87 0F 00                  call 0x1404f5698
003FCF6E  44 0F 22 C3                     mov cr8, rbx
003FCF72  48 83 C4 20                     add rsp, 0x20
003FCF76  5B                              pop rbx
003FCF77  C3                              ret
003FCF78  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KzLowerIrql(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 12361155)) != 0) {
        a1 = v_cr8;
        a2 = a1;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KzLowerIrql(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xBC9DC3)) != 0) {
        Arg1 = v_cr8;
        a2 = Arg1;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FCF50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FCF50[BB_003FCF50]
  bb_003FCF62[BB_003FCF62]
  bb_003FCF6E[BB_003FCF6E]
  bb_003FCF78[BB_003FCF78]
  bb_003FCF50 -->|branch| bb_003FCF6E
  bb_003FCF50 -->|fallthrough| bb_003FCF62
  bb_003FCF62 -->|flow| bb_003FCF6E
```
