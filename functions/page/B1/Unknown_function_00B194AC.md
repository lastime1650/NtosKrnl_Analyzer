# sub_00B194AC

- RVA: `0x00B194AC`–`0x00B194D3` (길이 `39` bytes)
- VA: `0x0000000140B194AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007DC04`
- 디코드: `10`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B194AF` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00B194BB` → [AlpcpEndInitialization](../A2/AlpcpEndInitialization_function_00A20C78.md) (function, `0x00A20C78`)
- `0x00B194C8` → [AlpcpDereferenceBlobEx](../88/AlpcpDereferenceBlobEx_function_0088AF00.md) (function, `0x0088AF00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B194AF` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B194CE` → [AlpcpCreateReserve + 0x262](../89/AlpcpCreateReserve_function_00892318.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B194AC  48 8B CB                        mov rcx, rbx
00B194AF  E8 4C 81 7C FF                  call 0x1402e1600
00B194B4  48 8B CF                        mov rcx, rdi
00B194B7  4C 89 67 08                     mov qword ptr [rdi + 8], r12
00B194BB  E8 B8 77 F0 FF                  call 0x140a20c78
00B194C0  BA 02 00 00 00                  mov edx, 2
00B194C5  48 8B CF                        mov rcx, rdi
00B194C8  E8 33 1A D7 FF                  call 0x14088af00
00B194CD  90                              nop
00B194CE  E9 A7 90 D7 FF                  jmp 0x14089257a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B194AC(void)
{
    __int64 result;

    result = KeAbPostRelease(v_rbx, a2, a3, a4);
    *(unsigned __int64 *)(v_rdi + 8) = v_r12;
    result = AlpcpEndInitialization(v_rdi, a2, a3, a4);
    result = AlpcpDereferenceBlobEx(v_rdi, 2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B194AC(void)
{
    int64_t result;

    result = KeAbPostRelease(local_rbx, a2, a3, a4);
    *(uint64_t *)(local_rdi + 0x8) = local_r12;
    result = AlpcpEndInitialization(local_rdi, a2, a3, a4);
    result = AlpcpDereferenceBlobEx(local_rdi, 2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B194AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B194AC[BB_00B194AC]
```
