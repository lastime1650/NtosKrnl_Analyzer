# sub_00397301

- RVA: `0x00397301`–`0x00397328` (길이 `39` bytes)
- VA: `0x0000000140397301`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081344`
- 디코드: `9`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0039730F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0039731E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00397301` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00397309` → [sub_00397241 + 0x3A](Unknown_function_00397241.md) (`tail-transfer`)
  - `0x00397316` → [sub_00397241 + 0x3A](Unknown_function_00397241.md) (`tail-transfer`)
  - `0x00397323` → [sub_00397241 + 0x3C](Unknown_function_00397241.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00397301  8B 05 B1 F7 C2 00               mov eax, dword ptr [rip + 0xc2f7b1]
00397307  A8 40                           test al, 0x40
00397309  0F 84 6C FF FF FF               je 0x14039727b
0039730F  E8 7C 81 F7 FF                  call 0x14030f490
00397314  84 C0                           test al, al
00397316  0F 84 5F FF FF FF               je 0x14039727b
0039731C  8B CE                           mov ecx, esi
0039731E  E8 3D 81 F7 FF                  call 0x14030f460
00397323  E9 55 FF FF FF                  jmp 0x14039727d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00397301(void)
{
    __int64 result;

    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, a3, a4);
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00397301(void)
{
    int64_t result;

    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, a3, a4);
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00397301&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00397301[BB_00397301]
  bb_0039730F[BB_0039730F]
  bb_0039731C[BB_0039731C]
  bb_00397301 -->|fallthrough| bb_0039730F
  bb_0039730F -->|fallthrough| bb_0039731C
```
