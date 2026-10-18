# ZwAlpcAcceptConnectPort

- RVA: `0x006ADFF0`–`0x006AE00F` (길이 `31` bytes)
- VA: `0x00000001406ADFF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C043C`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DifZwAlpcAcceptConnectPortWrapper](../63/DifZwAlpcAcceptConnectPortWrapper_function_0063DA50.md) at `0x0063DB96`
- [SshpAlpcProcessAlpcMessage](../../page/77/SshpAlpcProcessAlpcMessage_function_0077506C.md) at `0x0077518A`
- [SshpAlpcProcessAlpcMessage](../../page/77/SshpAlpcProcessAlpcMessage_function_0077506C.md) at `0x007751C5`
- [SepRmLsaConnectRequest](../../page/A6/SepRmLsaConnectRequest_function_00A6AB54.md) at `0x00A6AC37`
- [SepRmLsaConnectRequest](../../page/A6/SepRmLsaConnectRequest_function_00A6AB54.md) at `0x00A6AD06`
- [sub_00B39570](../../page/B3/Unknown_function_00B39570.md) at `0x00B395E0`
- [sub_00B39570](../../page/B3/Unknown_function_00B39570.md) at `0x00B3961D`
- [sub_00B47C52](../../page/B4/Unknown_function_00B47C52.md) at `0x00B47CCA`
- [sub_00B47C52](../../page/B4/Unknown_function_00B47C52.md) at `0x00B47D0D`

### Static image references
- `0x006ADFFC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AE009` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ADFF0  48 8B C4                        mov rax, rsp
006ADFF3  FA                              cli
006ADFF4  48 83 EC 10                     sub rsp, 0x10
006ADFF8  50                              push rax
006ADFF9  9C                              pushfq
006ADFFA  6A 10                           push 0x10
006ADFFC  48 8D 05 5D 54 00 00            lea rax, [rip + 0x545d]
006AE003  50                              push rax
006AE004  B8 79 00 00 00                  mov eax, 0x79
006AE009  E9 B2 69 01 00                  jmp 0x1406c49c0
006AE00E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwAlpcAcceptConnectPort(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwAlpcAcceptConnectPort(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ADFF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ADFF0[BB_006ADFF0]
  bb_006AE00E[BB_006AE00E]
```
